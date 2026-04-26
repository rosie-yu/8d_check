# 8D Report Evaluator

使用 LLM 對 8D 報告進行自動評分，並將結果視覺化呈現。

## 專案結構

```text
.
├── run_eightd_evaluator.ipynb  # 執行評分流程
├── eightd_evaluator.py         # 評分邏輯
├── ui.py                       # 結果展示 / 圖表
└── data/
    ├── 8d_data.xlsx            # 輸入資料(報告內容、評分標準)
    └── scored_report.xlsx      # 評分結果
    
```

## 使用方式

### 1. 執行評分
執行 `run_eightd_evaluator.ipynb`
讀取 `data/8d_data.xlsx` → 呼叫 `eightd_evaluator.py` 評分 → 輸出 `data/scored_report.xlsx`

#### 評分邏輯
每個評分項目獨立呼叫一次 LLM。

**Input**
- 評分項目 (如: Cause of Occurrence)
- 報告內容 (如: 經確認為供應商來料異常...)
- 評分準則 (如: 差劣 (0-5分)： 5W 條件僅包含...)

**Output**
- 分數
- 原因
- 改善建議

### 2. 查看結果
```bash
streamlit run ui.py
```

讀取 `data/scored_report.xlsx`，顯示評分結果與分析圖表。

## API Key
建議使用 `.env`：

```env
GOOGLE_API_KEY=your_key
```