<img src="banner.svg" alt="Leng Niu / game server developer" width="100%">

專注在線上遊戲的伺服器端：封包協定、遊戲邏輯、經濟系統，以及營運用的管理工具。也做 2D 遊戲用的地圖、圖片與字型工具。

I work on the server side of online games: network protocols, game logic, in-game economies and the tools that keep a live server running. I also build tools for 2D game assets: maps, sprites and fonts.

### ▌擅長 / Focus

- 伺服器架構：連線管理、頻道與地圖分流、排程與資料存檔
- 封包協定：解析、設計與相容舊版客戶端
- 遊戲系統：任務、副本、交易、小遊戲與活動
- 營運工具：GM 主控台、機器人、監控與自動更新
- 資料庫：MySQL／SQL Server 結構設計、備份與效能調整

### ▌連線與協定 / Networking

| 專案 | 說明 |
| --- | --- |
| [sidescroll-net](https://github.com/vtxe02023274/sidescroll-net)<br>[試玩](https://vtxe02023274.github.io/sidescroll-net/) | 橫向捲軸多人連線：權威伺服器、客戶端預測（修正量 0）、內插、延遲補償、快照差量與視野裁切。Authoritative server for 2D side-scrolling multiplayer with prediction, interpolation, lag compensation and delta snapshots. |
| [pktspec](https://github.com/vtxe02023274/pktspec) | 用一份 YAML 描述遊戲封包，產生 Java 讀寫程式與文件。Describe game packets once in YAML, generate Java encoders/decoders and docs. |

### ▌2D 遊戲工具 / 2D game tools

| 專案 | 說明 |
| --- | --- |
| [isotiles](https://github.com/vtxe02023274/isotiles)<br>[試用](https://vtxe02023274.github.io/isotiles/) | 網頁版等角與交錯式地圖編輯器，讀寫 Tiled 地圖，渲染與 Tiled 逐像素一致。Isometric and staggered map editor in the browser, reads and writes Tiled maps. |
| [aseview](https://github.com/vtxe02023274/aseview)<br>[試用](https://vtxe02023274.github.io/aseview/) | Aseprite 檢視與匯出：sprite sheet、逐標籤 GIF、放大、逐圖層，網頁與命令列都能用。View Aseprite files and export sheets, GIFs, scaled and per-layer, in the browser or from the command line. |
| [fntview](https://github.com/vtxe02023274/fntview)<br>[試用](https://vtxe02023274.github.io/fntview/) | BMFont 點陣字型檢查、轉檔，支援 SDF／MSDF，也能從 .ttf 產生字型。Check, convert and make BMFont bitmap fonts, including SDF and MSDF. |
| [tiledcheck](https://github.com/vtxe02023274/tiledcheck) | Tiled 地圖檢查：缺檔、超出範圍的圖塊、重疊的 tileset、沒用到的 tileset，可放進 GitHub Actions。Lint Tiled maps locally or in CI. |

### ▌常用技術 / Stack

`Java` `C++` `C#` `TypeScript` `MySQL` `SQL Server` `Netty` `Windows Server`
