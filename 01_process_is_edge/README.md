# Chapter 1: The Process Is Your Edge

# 第 1 章:流程就是你的優勢

The chapter establishes the chapter's central claim: in trading, durable performance depends less on picking a sophisticated model than on maintaining a disciplined research process that can survive changing markets, noisy signals, and real-world frictions. It gives readers a usable vocabulary for market change, shows why recent shocks exposed fragile assumptions, and reframes ML for trading as an adaptation problem rather than a model-selection contest.

本章確立了全章的核心主張:在交易中,能否長期維持績效,與其說取決於挑選到多精密的模型,不如說取決於能否維持一套有紀律的研究流程,讓它撐得過不斷變化的市場、充滿雜訊的訊號,以及現實世界中的各種摩擦成本。本章提供讀者一套描述市場變化的實用詞彙,說明近年的衝擊事件為何暴露出脆弱的假設,並把機器學習交易重新定位為一個「適應」問題,而不是一場模型選擇的競賽。

## Learning Objectives

* Distinguish structural breaks, regimes, data drift, concept drift, and online detection, and explain why static trading models degrade in changing markets
* Explain the ML4T Workflow as a research-to-production system, including its data infrastructure foundation, scoping invariants, iterative research modules, and feedback loops from live trading back to research
* Define the evidence boundary between exploration and confirmation, and explain how trial logging, sealed holdouts, and selection-aware evaluation preserve research integrity
* Describe how causal inference and generative AI fit within a disciplined trading workflow, including the main benefits they provide and the new failure modes they introduce
* Apply regime thinking, implementability checks, and monitoring logic to diagnose strategy vulnerabilities and to adapt workflow discipline across independent and institutional settings

## 學習目標

* 區分結構性斷裂(structural break)、市場狀態(regime)、資料漂移(data drift)、概念漂移(concept drift)與線上偵測(online detection),並解釋為什麼靜態的交易模型會在不斷變化的市場中逐漸失效
* 說明 ML4T 工作流程是一套從研究到上線的系統,包括它的資料基礎建設、界定範圍時的不變條件、反覆迭代的研究模組,以及從實盤交易回饋到研究的回饋迴路
* 定義「探索」與「確認」之間的證據界線,並解釋試驗紀錄、封存的保留樣本(sealed holdout),以及把挑選過程納入考量的評估方式,如何維護研究的可信度
* 描述因果推論與生成式 AI 如何放進一套有紀律的交易工作流程,包括它們帶來的主要好處,以及它們引入的新失敗模式
* 運用市場狀態的思維、可執行性檢查與監控邏輯來診斷策略的弱點,並依個人與機構的不同情境調整工作流程的紀律

## Sections

## 各節內容

### 1.1 Why process discipline matters

This section establishes the chapter's central claim: in trading, durable performance depends less on picking a sophisticated model than on maintaining a disciplined research process that can survive changing markets, noisy signals, and real-world frictions. It gives readers a usable vocabulary for market change, shows why recent shocks exposed fragile assumptions, and reframes ML for trading as an adaptation problem rather than a model-selection contest.

### 1.1 為什麼流程紀律很重要

本節確立全章的核心主張:在交易中,能否長期維持績效,與其說取決於挑選到多精密的模型,不如說取決於能否維持一套有紀律的研究流程,讓它撐得過不斷變化的市場、充滿雜訊的訊號,以及現實世界中的各種摩擦成本。本節提供讀者一套描述市場變化的實用詞彙,說明近年的衝擊事件為何暴露出脆弱的假設,並把機器學習交易重新定位為一個「適應」問題,而不是一場模型選擇的競賽。

### 1.2 Introducing the ML4T workflow

This section presents the book's core framework: a research-to-production workflow built on point-in-time-correct data infrastructure, explicit scoping rules, iterative feature and model development, realistic strategy design, deployment discipline, and ongoing monitoring. The key value for readers is that it turns trading research into a managed lifecycle with auditable artifacts, clear handoffs, and an explicit boundary between exploration and confirmation.

### 1.2 介紹 ML4T 工作流程

本節介紹全書的核心架構:一套從研究到上線的工作流程,建立在時點正確(point-in-time-correct)的資料基礎建設、明確的範圍界定規則、反覆迭代的特徵與模型開發、貼近現實的策略設計、部署紀律,以及持續的監控之上。對讀者最重要的價值在於,它把交易研究變成一個受管理的生命週期,其中有可稽核的產出物、清楚的交接點,以及「探索」與「確認」之間明確的界線。

### 1.3 Causal inference and generative AI in the workflow

This section places two modern method families inside the workflow rather than treating them as standalone trends. Causal inference is framed as a way to sharpen mechanisms, assumptions, and diagnosis; generative AI is framed as a way to expand research and unstructured-data processing while also creating new risks such as leakage, hallucination, and workflow bloat. Readers should care because the section makes clear that new tools increase the value of discipline rather than replacing it.

### 1.3 工作流程中的因果推論與生成式 AI

本節把兩類現代方法放進工作流程之中,而不是把它們當成各自獨立的潮流。因果推論被定位為一種讓機制、假設與診斷更加精確的方法;生成式 AI 則被定位為一種擴大研究範圍與非結構化資料處理能力的方法,但同時也帶來新的風險,例如資訊洩漏(leakage)、幻覺(hallucination)與工作流程膨脹。讀者之所以應該在意,是因為本節清楚指出:新工具提高了紀律的價值,而不是取代紀律。

### 1.4 Keeping up with changing market regimes

This section turns non-stationarity into something operational. It shows how regime concepts can support explanation, robustness checks, and live monitoring, while insisting that regimes are primarily a risk lens rather than a reliable timing signal. The factor and macro examples make the idea concrete: regime methods are useful when they help identify adverse environments and connect them to predefined risk actions.

- [`factor_regimes`](factor_regimes.ipynb) — Demonstrates unsupervised learning for market regime detection using Gaussian Mixture Models (GMM) on factor returns from the AQR Century of Factor Premia dataset.
- [`macro_regimes`](macro_regimes.ipynb) — Demonstrates unsupervised learning for market regime detection using macroeconomic indicators from FRED, validated against S&P 500 volatility and drawdowns.

### 1.4 跟上不斷變化的市場狀態

本節把非定態性(non-stationarity)變成可以實際操作的東西。它說明市場狀態的概念如何支援解釋、穩健性檢查與實盤監控,同時堅持市場狀態主要是一面觀察風險的透鏡,而不是可靠的擇時訊號。因子與總體經濟的範例讓這個概念具體起來:當市場狀態方法能幫助辨識不利的環境,並把它們連結到預先定義好的風險行動時,這些方法才有用。

- [`factor_regimes`](factor_regimes.ipynb) — 示範以非監督式學習偵測市場狀態:對 AQR Century of Factor Premia 資料集的因子報酬使用高斯混合模型(GMM)。
- [`macro_regimes`](macro_regimes.ipynb) — 示範以非監督式學習偵測市場狀態:使用 FRED 的總體經濟指標,並以 S&P 500 的波動度與回撤加以驗證。

### 1.5 Independent versus institutional workflows in the real world

This section translates the workflow into real operating contexts. It explains how institutions benefit from built-in friction and review, while independent researchers must create their own governance through documentation, checkpoints, and explicit stop criteria. The practical payoff is strong: it helps readers see where solo practitioners are vulnerable, where they can still compete, and how reusable infrastructure compounds research quality over time.

### 1.5 現實世界中個人與機構的工作流程

本節把工作流程放到實際的運作情境中。它解釋機構如何受益於內建的摩擦與審查機制,而獨立研究者則必須透過文件紀錄、檢查點與明確的停止條件,自己建立治理機制。實務上的收穫很大:它幫助讀者看清個人從業者在哪些地方容易出問題、在哪些地方仍然具有競爭力,以及可重複使用的基礎建設如何隨時間讓研究品質產生複利效果。

## Running the Notebooks

## 執行筆記本

```bash
# From the repository root
# 從儲存庫根目錄執行
uv run python 01_process_is_edge/<notebook>.py

# Test mode (reduced data via Papermill)
# 測試模式(透過 Papermill 使用縮減後的資料)
uv run pytest tests/test_chapter_notebooks.py -v -k "01_process_is_edge"
```

## References

## 參考文獻

- **Andrew Ang and Geert Bekaert** (2002). [International Asset Allocation With Regime Shifts](https://doi.org/10.1093/rfs/15.4.1137). *Review of Financial Studies*.
- **Robert D. Arnott et al.** (2018). [A Backtesting Protocol in the Era of Machine Learning](https://doi.org/10.2139/ssrn.3275654).
- **Darrell Duffie** (2020). [Still the World's Safe Haven? Redesigning the U.S. Treasury Market After the COVID-19 Crisis](https://www.brookings.edu/wp-content/uploads/2020/05/WP62_Duffie_v2.pdf).
- **David Easley et al.** (2012). [The Volume Clock: Insights into the High Frequency Paradigm](https://doi.org/10.2139/ssrn.2034858).
- **Frank J. Fabozzi et al.** (2024). [Paradigm Shift: Embracing Holism in Causal Modeling for Investment Applications](https://doi.org/10.3905/jpm.2024.51.1.159). *The Journal of Portfolio Management*.
- **Frank J. Fabozzi and Caleb C. Stenholm** (2025). [Strategic Discipline: How Asset Management Mirrors Military Operations](https://doi.org/10.3905/jpm.2025.1.769). *The Journal of Portfolio Management*.
- **Ziang Fang and Jason Moore** (2025). What AI Can (and Can't Yet) Do for Alpha.
- **Stefano Giglio et al.** (2022). [Factor Models, Machine Learning, and Asset Pricing](https://doi.org/10.1146/annurev-financial-101521-104735). *Annual Review of Financial Economics*.
- **Campbell R. Harvey et al.** (2016). [...and the Cross-Section of Expected Returns](https://doi.org/10.1093/rfs/hhv059). *Review of Financial Studies*.
- **Blanka Horvath et al.** (2021). [Clustering Market Regimes Using the Wasserstein Distance](https://doi.org/10.2139/ssrn.3947905).
- **Antti Ilmanen et al.** (2021). [How Do Factor Premia Vary Over Time? A Century of Evidence](https://doi.org/10.2139/ssrn.3400998).
- **Justina Lee** (2025). [Man Group Says Agentic AI Is Now Devising Quant Trading Signals](https://www.bloomberg.com/news/articles/2025-07-10/man-group-says-agentic-ai-is-now-devising-quant-trading-signals). *Bloomberg.com*.
- **Andrew W. Lo** (2004). [The Adaptive Markets Hypothesis: Market Efficiency from an Evolutionary Perspective](https://papers.ssrn.com/abstract=602222).
- **Martin Luk** (2023). [Generative AI: Overview, Economic Impact, and Applications in Asset Management](https://doi.org/10.2139/ssrn.4574814).
- **Judea Pearl** (2019). [The seven tools of causal inference, with reflections on machine learning](https://doi.org/10.1145/3241036). *Communications of the ACM*.
- **Marcos López de Prado** (2018). The 10 Reasons Most Machine Learning Funds Fail. *The Journal of Portfolio Management*.
- **Marcos Lopez de Prado et al.** (2024). [The Case for Causal Factor Investing](https://doi.org/10.2139/ssrn.4774522).
- **Marcos López de Prado and Vincent Zoonekynd** (2025). [Correcting the Factor Mirage: A Research Protocol for Causal Factor Investing](https://doi.org/10.3905/jpm.2025.1.794). *The Journal of Portfolio Management*.
- **James Ryseff et al.** (2024). [The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed: Avoiding the Anti-Patterns of AI](https://www.rand.org/pubs/research_reports/RRA2680-1.html).
- **Bernhard Schölkopf et al.** (2021). [Towards Causal Representation Learning](https://doi.org/10.48550/arXiv.2102.11107).
- **Stefan Studer et al.** (2021). [Towards CRISP-ML(Q): A Machine Learning Process Model with Quality Assurance Methodology](https://doi.org/10.3390/make3020020). *Machine Learning and Knowledge Extraction*.
- **A. Sinem Uysal and John M. Mulvey** (2021). [A Machine Learning Approach in Regime-Switching Risk Parity Portfolios](https://doi.org/10.3905/jfds.2021.1.057). *The Journal of Financial Data Science*.
