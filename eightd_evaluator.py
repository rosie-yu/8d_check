from dotenv import load_dotenv
import os
import ast
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = genai.GenerativeModel("gemini-2.5-flash")

def evaluate(data, guide, check_item):
    df = data.set_index('項目').copy()
    
    # 檢查欄位 (應移到上傳data時檢查)
    cols = list(df.index)
    is_contained = set(check_item).issubset(cols)
    assert is_contained==True, '缺少欄位'

    # llm 評分
    data_dict = df.to_dict()['原始內容']
    score_dict = guide.set_index('項目').to_dict()['評核標準']
    results = {}
    for item,guide in score_dict.items():
        data = data_dict[item]
        result = llm_score(item, data, guide)
        result_score = result['score']
        result_reason = result['reason']
        result_suggestion = result['suggestion']
        result_dict = {item:result}
        results.update(result_dict)

    # 結果存進 df
    for item in results:
        df.loc[item, ["score", "reason", "suggestion"]] = [results[item]["score"],results[item]["reason"],results[item]["suggestion"]]
    return df

def llm_score(item, data, guide):
    prompt = f"""
    根據評分標準評分。

    項目: {item}
    內容: {data}
    評分準則: {guide}

    回傳JSON:
    {{
        "score": 分數,
        "reason": "原因",
        "suggestion": "改善建議",
    }}
    """
    response = MODEL.generate_content(prompt)
    
    # 處理回傳結果
    response_text = response.text.strip()
    response_text = response_text.replace("```json", "").replace("```", "").strip()
    response_dict = ast.literal_eval(response_text)
    return response_dict

def classify_score(score):
    if 0 <= score <= 5:
        return "差劣"
    elif 6 <= score <= 10:
        return "普通"
    elif 11 <= score <= 15:
        return "不錯"
    elif 16 <= score <= 20:
        return "傑出"
    else:
        return None