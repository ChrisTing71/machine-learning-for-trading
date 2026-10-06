# 中文翻譯的維護工具

這個資料夾保存各章筆記本的中文譯文,以及把譯文插回筆記本的腳本。用途是在合併原始專案(upstream)的更新之後,把中文儲存格重新放回去。

## 內容

- `zh_tool.py`:腳本,有 `dump`、`extract`、`apply` 三個指令。
- `<章節資料夾>/<筆記本名稱>.txt`:該筆記本的中文譯文,每個英文 markdown 儲存格一段,以 `=====<儲存格 id>` 開頭。

## 合併 upstream 時筆記本發生衝突怎麼辦

`.ipynb` 是 JSON,衝突很難手動解。做法是該本先採用 upstream 的版本,再把中文插回去:

```bash
git fetch upstream
git merge upstream/main

# 對每一本有衝突的筆記本:
git checkout --theirs 02_financial_data_universe/01_us_equities_eda.ipynb
python translations/zh/zh_tool.py apply \
    02_financial_data_universe/01_us_equities_eda.ipynb \
    translations/zh/02_financial_data_universe/01_us_equities_eda.txt
git add 02_financial_data_universe/01_us_equities_eda.ipynb
```

`apply` 會列出兩種需要人工處理的情況:

- **untranslated cells**:upstream 新增或改過 id 的儲存格,還沒有中文。
- **translations with no matching cell**:upstream 已刪除的儲存格,對應的譯文用不到了。

注意:`apply` 是依儲存格 id 對應的。如果 upstream 改了某個儲存格的英文內容但 id 沒變,舊的中文仍會被插回去,需要自己對照更新。

## 其他指令

```bash
# 印出某本筆記本的英文 markdown(翻譯新內容時用)
python translations/zh/zh_tool.py dump <notebook.ipynb>

# 手動改過筆記本裡的中文之後,把它存回譯文檔
python translations/zh/zh_tool.py extract <notebook.ipynb> <translation.txt>
```

README 與 `導讀.md` 是一般文字檔,衝突時直接手動解即可,不在這套工具的範圍內。
