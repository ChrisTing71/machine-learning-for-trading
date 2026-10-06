# Chapter 2: The Financial Data Universe

# 第 2 章:金融資料的全貌

The chapter gives readers the conceptual map they need before touching any dataset. Its key contribution is not just the market / fundamental / alternative taxonomy, but the claim that every dataset embeds definitions about timestamps, adjustments, identifiers, and revisions, and that these choices determine what the data actually means in research.

本章提供讀者在接觸任何資料集之前所需要的概念地圖。它的主要貢獻不只是「市場/基本面/另類」這套分類法,更在於這項主張:每個資料集都內含關於時間戳記、價格調整、識別碼與修訂方式的定義,而這些選擇決定了資料在研究中真正的意義。

## Learning Objectives

* Distinguish among market, fundamental, and alternative data, and explain how dataset definitions shape what each source means in research and trading applications
* Compare the observability, conventions, and engineering constraints of major asset classes, and identify how market structure changes what can be measured and modeled
* Apply a financial data quality framework to diagnose common failure modes, especially point-in-time violations, survivorship bias, corporate action errors, and identifier mismatches
* Conduct vendor due diligence across data quality, legal and compliance, and technical and commercial dimensions
* Choose storage and query architectures that fit research and production needs, including when to use partitioned files, embedded analytical databases, or server-based systems

## 學習目標

* 區分市場資料、基本面資料與另類資料,並解釋資料集的定義如何影響每種來源在研究與交易應用中的意義
* 比較主要資產類別的可觀測性、慣例與工程限制,並辨識市場結構如何改變可以量測與建模的內容
* 運用金融資料品質架構來診斷常見的失敗模式,尤其是時點(point-in-time)違規、倖存者偏誤、公司行動錯誤與識別碼不符
* 從資料品質、法律與法遵、技術與商業等面向,對供應商進行盡職調查
* 選擇符合研究與正式環境需求的儲存與查詢架構,包括何時使用分割檔案、內嵌式分析資料庫或伺服器型系統

## Sections

## 各節內容

### 2.1 A Modern Taxonomy of Financial Data

This section gives readers the conceptual map they need before touching any dataset. Its key contribution is not just the market / fundamental / alternative taxonomy, but the claim that every dataset embeds definitions about timestamps, adjustments, identifiers, and revisions, and that these choices determine what the data actually means in research.

### 2.1 金融資料的現代分類法

本節提供讀者在接觸任何資料集之前所需要的概念地圖。它的主要貢獻不只是「市場/基本面/另類」這套分類法,更在於這項主張:每個資料集都內含關於時間戳記、價格調整、識別碼與修訂方式的定義,而這些選擇決定了資料在研究中真正的意義。

### 2.2 The Asset-Class Market Data Landscape

This section broadens the discussion from data categories to the practical reality that "price," "liquidity," and even "the dataset" mean different things across equities, ETPs, futures, options, digital assets, FX, fixed income, swaps, and commodities. Its value is comparative: it helps readers understand why engineering choices are inseparable from market structure.

- [`01_us_equities_eda`](01_us_equities_eda.ipynb) — This notebook introduces the Wiki Prices dataset - a survivorship-bias-free collection of US equity prices. Understanding survivorship bias is critical for realistic backtesting.
- [`02_corporate_actions`](02_corporate_actions.ipynb) — This notebook demonstrates how stock splits and dividends break historical price series, and shows the industry-standard backward adjustment methodology used by major data vendors. Correctly adjusting for corporate actions is essential for any ML model using return-based features.
- [`03_etfs_eda`](03_etfs_eda.ipynb) — This notebook introduces the 50-ETF universe that serves as the foundation for the ETF Rotational Momentum case study throughout the book. We explore the schema, coverage, categories, and data quality characteristics.
- [`04_cme_futures_eda`](04_cme_futures_eda.ipynb) — This notebook introduces the CME futures dataset shipped with the book. It demonstrates the data structure, coverage, and key concepts for working with futures data.
- [`05_futures_session_aggregation`](05_futures_session_aggregation.ipynb) — This notebook converts hourly continuous futures data (stored in UTC) to session-aware daily bars. CME futures sessions end at 4:00 PM Central Time, so daily bars must respect this boundary—not midnight UTC.
- [`06_futures_continuous`](06_futures_continuous.ipynb) — This notebook tackles one of the most critical challenges in futures analysis: creating continuous price series from individual expiring contracts. We implement roll detection algorithms and adjustment methods (Panama, ratio) to eliminate artificial price gaps while preserving accurate return characteristics.
- [`07_sp500_options_eda`](07_sp500_options_eda.ipynb) — This notebook provides a comprehensive exploration of the AlgoSeek S&P 500 Options Analytics dataset. Options data is fundamentally different from spot market data—it contains forward-looking information about expected volatility, directional sentiment, and tail risk that isn't directly observable in underlying prices.
- [`08_options_greeks_computation`](08_options_greeks_computation.ipynb) — This notebook derives and implements the Black-Scholes option pricing framework from first principles. We compute implied volatility and all Greeks, then validate our calculations against the pre-computed values in the AlgoSeek options data.
- [`09_options_continuous`](09_options_continuous.ipynb) — Options are time-decaying instruments. Unlike equities or futures, an option's price reflects both the value of the underlying exposure and the remaining time to expiration.
- [`10_crypto_perps_eda`](10_crypto_perps_eda.ipynb) — This notebook introduces the cryptocurrency dataset from Binance Futures. We explore hourly OHLCV data and the Premium Index (perpetual futures vs spot spread) that forms the basis for the Crypto Premium Arbitrage case study.
- [`11_crypto_premium_analysis`](11_crypto_premium_analysis.ipynb) — This notebook demonstrates how to work with Binance perpetual futures premium index data - the foundation for funding rate arbitrage strategies. We load, explore, and analyze premium dynamics across major cryptocurrencies to identify potential arbitrage opportunities.
- [`12_fx_pairs_eda`](12_fx_pairs_eda.ipynb) — This notebook introduces the FX dataset from OANDA. FX markets are OTC with no centralized exchange, so prices aggregate from multiple liquidity providers.

### 2.2 各資產類別的市場資料概況

本節把討論從資料類別擴大到實務上的現實:「價格」、「流動性」甚至「資料集」本身,在股票、ETP、期貨、選擇權、數位資產、外匯、固定收益、交換與商品之間的意義各不相同。它的價值在於比較:幫助讀者理解為什麼工程上的選擇與市場結構密不可分。

- [`01_us_equities_eda`](01_us_equities_eda.ipynb) — 介紹 Wiki Prices 資料集——一份號稱沒有倖存者偏誤的美國股票價格資料。理解倖存者偏誤對於做出貼近現實的回測至關重要。
- [`02_corporate_actions`](02_corporate_actions.ipynb) — 示範股票分割與股利如何破壞歷史價格序列,並說明主要資料供應商採用的業界標準向後調整法。正確調整公司行動,對任何使用報酬類特徵的 ML 模型都不可或缺。
- [`03_etfs_eda`](03_etfs_eda.ipynb) — 介紹作為全書 ETF 輪動動能案例研究基礎的 ETF 股票池。我們探索它的結構、涵蓋範圍、類別與資料品質特性。
- [`04_cme_futures_eda`](04_cme_futures_eda.ipynb) — 介紹隨書提供的 CME 期貨資料集。示範資料結構、涵蓋範圍,以及處理期貨資料的關鍵概念。
- [`05_futures_session_aggregation`](05_futures_session_aggregation.ipynb) — 把小時頻率的連續期貨資料(以 UTC 儲存)轉換成依交易時段劃分的日 K 棒。CME 期貨的交易時段在美國中部時間下午 4:00 結束,所以日 K 棒必須遵守這個邊界,而不是 UTC 午夜。
- [`06_futures_continuous`](06_futures_continuous.ipynb) — 處理期貨分析中最關鍵的挑戰之一:從會到期的個別合約建立連續價格序列。我們實作轉倉偵測演算法與調整方法(Panama、比率),以消除人為的價格缺口,同時保留正確的報酬特性。
- [`07_sp500_options_eda`](07_sp500_options_eda.ipynb) — 全面探索 AlgoSeek 的 S&P 500 選擇權分析資料集。選擇權資料與現貨市場資料有根本上的不同——它包含關於預期波動度、方向性情緒與尾部風險的前瞻性資訊,這些在標的價格中無法直接觀察到。
- [`08_options_greeks_computation`](08_options_greeks_computation.ipynb) — 從基本原理推導並實作 Black-Scholes 選擇權定價架構。我們計算隱含波動度與所有 Greeks,再對照 AlgoSeek 選擇權資料中預先算好的數值驗證我們的計算。
- [`09_options_continuous`](09_options_continuous.ipynb) — 選擇權是會隨時間耗損的工具。與股票或期貨不同,選擇權的價格同時反映標的曝險的價值與距到期的剩餘時間。
- [`10_crypto_perps_eda`](10_crypto_perps_eda.ipynb) — 介紹來自 Binance Futures 的加密貨幣資料集。我們探索小時 OHLCV 資料與溢價指數(永續期貨與現貨的價差),後者是加密貨幣溢價套利案例研究的基礎。
- [`11_crypto_premium_analysis`](11_crypto_premium_analysis.ipynb) — 示範如何處理 Binance 永續期貨的溢價指數資料——資金費率套利策略的基礎。我們載入、探索並分析主要加密貨幣的溢價動態,以找出潛在的套利機會。
- [`12_fx_pairs_eda`](12_fx_pairs_eda.ipynb) — 介紹來自 OANDA 的外匯資料集。外匯市場是櫃檯買賣(OTC)市場,沒有集中交易所,所以價格是由多個流動性提供者彙總而來。

### 2.3 A Due Diligence Framework for Data Sourcing

This is the chapter's risk-control core. It explains that many apparent research successes are manufactured by data defects, then organizes due diligence around general quality dimensions, finance-specific failure modes, vendor evaluation, and internal governance. The section turns abstract warnings into operational rules: point-in-time correctness, survivorship handling, corporate action methodology, identifier integrity, legal rights, and reproducible versioning.

- [`13_data_quality_framework`](13_data_quality_framework.ipynb) — The ml4t-data library provides purpose-built tools for financial data quality. This notebook demonstrates the complete data quality workflow: Uses us_equities data.
- [`14_point_in_time_validation`](14_point_in_time_validation.ipynb) — Point-in-time correctness is essential for valid backtesting. Using information that wasn't available at decision time creates lookahead bias - making backtests look better than they would perform in live trading.
- [`15_survivorship_bias_detection`](15_survivorship_bias_detection.ipynb) — Survivorship bias is arguably the most dangerous form of data contamination in quantitative finance. This notebook uses real historical data from the US equities dataset (US Equities, originally Quandl WIKI) to demonstrate, detect, and quantify survivorship bias.
- [`16_provider_comparison`](16_provider_comparison.ipynb) — ML4T Third Edition - Chapter 2: The Financial Data...

### 2.3 資料來源的盡職調查架構

這是本章的風險控管核心。它說明許多表面上的研究成果其實是資料缺陷製造出來的,接著圍繞一般品質面向、金融特有的失敗模式、供應商評估與內部治理來組織盡職調查。本節把抽象的警告轉化成可操作的規則:時點正確性、倖存者偏誤的處理、公司行動的方法論、識別碼的完整性、法律權利,以及可重現的版本管理。

- [`13_data_quality_framework`](13_data_quality_framework.ipynb) — ml4t-data 函式庫提供專為金融資料品質打造的工具。本筆記本示範完整的資料品質工作流程。使用美國股票資料。
- [`14_point_in_time_validation`](14_point_in_time_validation.ipynb) — 時點正確性是有效回測的必要條件。使用決策當下還無法取得的資訊會造成前視偏誤——讓回測看起來比實盤交易的實際表現更好。
- [`15_survivorship_bias_detection`](15_survivorship_bias_detection.ipynb) — 倖存者偏誤可說是量化金融中最危險的資料污染形式。本筆記本使用美國股票資料集(原為 Quandl WIKI)的真實歷史資料,來示範、偵測並量化倖存者偏誤。
- [`16_provider_comparison`](16_provider_comparison.ipynb) — 示範如何用統一的介面從多個供應商取得資料,並比較各供應商之間的差異。

### 2.4 Storing Data

This section translates data discipline into infrastructure decisions. Rather than promoting a single stack, it explains how storage choice depends on access patterns, scale, concurrency, and operational maturity, and it benchmarks the trade-offs among file formats, embedded engines, and server databases. It gives readers a practical default architecture for modern research workflows while also teaching when more complex systems are justified.

- [`17_complete_pipeline`](17_complete_pipeline.ipynb) — This notebook demonstrates end-to-end data pipelines, bringing together concepts from this chapter: Uses crypto_perps, wiki_provider data.
- [`18_data_management`](18_data_management.ipynb) — Previous notebooks fetched and validated data. This notebook shows how to manage it at scale using ml4t-data's production features: Uses universe data.
- [`19_incremental_updates`](19_incremental_updates.ipynb) — The previous notebook introduced DataManager and HiveStorage. This notebook focuses on the update workflow — the core reason ml4t-data exists: Uses all, treasury_yields data.
- [`20_storage_benchmark_file`](20_storage_benchmark_file.ipynb) — Focus: Pure file format comparison (no query engines) Technologies: CSV, Parquet, Feather (Arrow IPC), HDF5 Operations: Write, Read (with forced materialization), Columnar...
- [`21_storage_benchmark_database`](21_storage_benchmark_database.ipynb) — > Docker required: This notebook depends on the benchmark environment and > database services.
- [`22_pandas_polars_benchmark`](22_pandas_polars_benchmark.ipynb) — DataFrame-engine comparison (pandas vs Polars) across read, filter, groupby, join, and lazy operations on synthetic financial data at S/M/L scales. Backs the in-memory engine-choice recommendation in §2.4.

### 2.4 儲存資料

本節把資料紀律轉化成基礎建設上的決策。它不推銷單一的技術組合,而是說明儲存方式的選擇如何取決於存取模式、規模、並行需求與營運成熟度,並對檔案格式、內嵌式引擎與伺服器資料庫之間的取捨進行效能測試。它為現代研究工作流程提供一個實用的預設架構,同時也教導何時值得採用更複雜的系統。

- [`17_complete_pipeline`](17_complete_pipeline.ipynb) — 示範端到端的資料管線,把本章的概念整合在一起。使用加密貨幣永續合約與 Wiki 供應商的資料。
- [`18_data_management`](18_data_management.ipynb) — 前面的筆記本抓取並驗證了資料。本筆記本說明如何使用 ml4t-data 的正式環境功能大規模地管理資料。
- [`19_incremental_updates`](19_incremental_updates.ipynb) — 上一本筆記本介紹了 DataManager 與 HiveStorage。本筆記本聚焦在更新流程——ml4t-data 存在的核心理由。
- [`20_storage_benchmark_file`](20_storage_benchmark_file.ipynb) — 重點:純檔案格式的比較(不含查詢引擎)。技術:CSV、Parquet、Feather(Arrow IPC)、HDF5。操作:寫入、讀取(強制實體化)、欄位讀取。
- [`21_storage_benchmark_database`](21_storage_benchmark_database.ipynb) — 需要 Docker:本筆記本依賴效能測試環境與資料庫服務。
- [`22_pandas_polars_benchmark`](22_pandas_polars_benchmark.ipynb) — DataFrame 引擎的比較(pandas 對上 Polars),涵蓋讀取、篩選、groupby、join 與延遲操作,在 S/M/L 三種規模的合成金融資料上進行。支持 §2.4 中關於記憶體內引擎選擇的建議。

## Running the Notebooks

## 執行筆記本

```bash
# From the repository root
# 從儲存庫根目錄執行
uv run python 02_financial_data_universe/<notebook>.py

# Test mode (reduced data via Papermill)
# 測試模式(透過 Papermill 使用縮減後的資料)
uv run pytest tests/test_chapter_notebooks.py -v -k "02_financial_data_universe"
```

### NB21 storage_benchmark_database prerequisites

`21_storage_benchmark_database` exercises 7 storage engines (DuckDB, SQLite, TimescaleDB, ClickHouse, QuestDB, PostgreSQL, Polars Parquet). Of these, **DuckDB and SQLite run locally** with no additional setup; the other five require the benchmark service stack to be running first:

```bash
docker compose --profile benchmark up -d
```

Without these services, NB21 silently falls back to the 2-engine subset (DuckDB + SQLite only) and the comparative server-database results in §2.4 will not be reproduced. Bring the stack down with `docker compose --profile benchmark down` when finished.

### NB21 storage_benchmark_database 的先備條件

`21_storage_benchmark_database` 會測試 7 個儲存引擎(DuckDB、SQLite、TimescaleDB、ClickHouse、QuestDB、PostgreSQL、Polars Parquet)。其中 **DuckDB 與 SQLite 可在本機執行**,不需要額外設定;其他五個則需要先啟動效能測試的服務:

```bash
docker compose --profile benchmark up -d
```

如果沒有這些服務,NB21 會默默退回只有 2 個引擎的子集(僅 DuckDB + SQLite),而 §2.4 中伺服器資料庫的比較結果就無法重現。完成後請用 `docker compose --profile benchmark down` 關閉這些服務。

## References

## 參考文獻

- **William Beaver et al.** (2007). [Delisting returns and their effect on accounting-based market anomalies](https://doi.org/10.1016/j.jacceco.2006.12.002). *Journal of Accounting and Economics*.
- **Florian Berg et al.** (2022). [Aggregate Confusion: The Divergence of ESG Ratings*](https://doi.org/10.1093/rof/rfac033). *Review of Finance*.
- **Mark M. Carhart et al.** (2002). [Mutual Fund Survivorship](https://doi.org/10.1093/rfs/15.5.1439). *The Review of Financial Studies*.
- **Lin William Cong et al.** (2023). [Crypto Wash Trading](https://doi.org/10.1287/mnsc.2021.02709). *Management Science*.
- **David Easley et al.** (2021). [Microstructure in the Machine Age](https://doi.org/10.1093/rfs/hhaa078). *The Review of Financial Studies*.
- **B. Espen Eckbo and Markus Lithell** (2025). [Merger-Driven Listing Dynamics](https://doi.org/10.1017/S0022109023001394). *Journal of Financial and Quantitative Analysis*.
- **Gene Ekster and Petter N. Kolm** (2020). [Alternative Data in Investment Management: Usage, Challenges and Valuation](https://doi.org/10.2139/ssrn.3715828).
- **Edwin J. Elton et al.** (1996). [Survivor Bias and Mutual Fund Performance](https://doi.org/10.1093/rfs/9.4.1097). *The Review of Financial Studies*.
- **Kingsley Y L Fong et al.** (2017). [What Are the Best Liquidity Proxies for Global Research?*](https://doi.org/10.1093/rof/rfx003). *Review of Finance*.
- **Songrun He et al.** (2024). [Fundamentals of Perpetual Futures](https://doi.org/10.48550/arXiv.2212.06888).
- **Jacques Joubert et al.** (2024). [The Three Types of Backtests](https://doi.org/10.2139/ssrn.4897573).
- **Nina Karnaukh et al.** (2015). [Understanding FX Liquidity](https://doi.org/10.2139/ssrn.2329738).
- **Gueorgui S. Konstantinov** (2025). [On Systematic Currency Management](https://doi.org/10.3905/jpm.2025.1.724). *The Journal of Portfolio Management*.
- **John Lehoczky and Mark Schervish** (2018). [Overview and History of Statistics for Equity Markets](https://doi.org/10.1146/annurev-statistics-031017-100518). *Annual Review of Statistics and Its Application*.
- **Alex Lipton and Marcos Lopez de Prado** (2020). [Three Quant Lessons from COVID-19](https://doi.org/10.2139/ssrn.3580185).
- **Tim Loughran and Bill McDonald** (2020). [Textual Analysis in Finance](https://doi.org/10.1146/annurev-financial-012820-032249). *Annual Review of Financial Economics*.
- **Yin Luo et al.** (2014). Seven Sins of Quantitative Investing.
- **Igor Makarov and Antoinette Schoar** (2020). [Trading and arbitrage in cryptocurrency markets](https://doi.org/10.1016/j.jfineco.2019.07.001). *Journal of Financial Economics*.
- **Hunter Ng et al.** (2025). [Price Discovery and Trading in Prediction Markets](https://doi.org/10.2139/ssrn.5331995).
- **Maureen O’Hara** (2015). [High frequency market microstructure](https://doi.org/10.1016/j.jfineco.2015.01.003). *Journal of Financial Economics*.
- **Marcos Lopez de Prado** (2018). Advances in Financial Machine Learning. *John Wiley & Sons*.
- **SEC** (2020). [Staff Report on Algorithmic Trading in U.S. Capital Markets](https://www.sec.gov/file/staff-report-algorithmic-trading-us-capital-markets).
- **Tyler Shumway** (1997). [The Delisting Bias in CRSP Data](https://doi.org/10.1111/j.1540-6261.1997.tb03818.x). *The Journal of Finance*.
- **David Vidal-Tomás** (2022). [Which cryptocurrency data sources should scholars use?](https://doi.org/10.1016/j.irfa.2022.102061). *International Review of Financial Analysis*.
