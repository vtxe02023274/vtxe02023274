<div align="center">

<img src="banner.svg" alt="Leng Niu: game server developer, netcode, protocols and 2D game tools" width="100%" />

<br/>

**English** · [繁體中文](#繁體中文)

</div>

### About me

- I work on the **server side of online games**: network protocols, game logic, in-game economies and the tools that keep a live server running
- I build **netcode** for real-time games: authoritative servers, client prediction, lag compensation and bandwidth tuning
- I make **2D game asset tools** for maps, sprites and bitmap fonts that run in the browser or on the command line
- I work with **MySQL / SQL Server** for game data: schema design, backups and performance

### Featured projects

<table>
<tr>
<td width="50%" valign="top">

#### [sidescroll-net](https://github.com/vtxe02023274/sidescroll-net)
Authoritative server for 2D side-scrolling multiplayer: client prediction with zero corrections, interpolation, lag compensation, delta snapshots and view culling.

`TypeScript` `WebSocket` · [**Live demo**](https://vtxe02023274.github.io/sidescroll-net/)

</td>
<td width="50%" valign="top">

#### [pktspec](https://github.com/vtxe02023274/pktspec)
Describe game packets once in YAML, then generate encoders and decoders for Java, C#, TypeScript and C++, a Wireshark dissector and a reference document. `diff` flags changes that break old clients and `fuzz` writes test corpora.

`TypeScript` `Java` `C#` `C++` `YAML`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [isotiles](https://github.com/vtxe02023274/isotiles)
Isometric and staggered map editor in the browser. Reads and writes Tiled maps and renders them pixel for pixel like Tiled.

`TypeScript` `Canvas` · [**Live demo**](https://vtxe02023274.github.io/isotiles/)

</td>
<td width="50%" valign="top">

#### [aseview](https://github.com/vtxe02023274/aseview)
View Aseprite files and export sprite sheets, GIFs per tag, scaled and per layer, in the browser or from the command line.

`TypeScript` `CLI` · [**Live demo**](https://vtxe02023274.github.io/aseview/)

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### [fntview](https://github.com/vtxe02023274/fntview)
Check, convert and make BMFont bitmap fonts, including SDF and MSDF, or build one from a .ttf.

`TypeScript` `Canvas` · [**Live demo**](https://vtxe02023274.github.io/fntview/)

</td>
<td width="50%" valign="top">

#### [tiledcheck](https://github.com/vtxe02023274/tiledcheck)
Lint Tiled maps for missing files, out of range tiles, overlapping or unused tilesets, locally or in GitHub Actions.

`TypeScript` `CLI` `GitHub Action`

</td>
</tr>
</table>

### Open source contributions

- [colyseus/schema#245](https://github.com/colyseus/schema/pull/245) (merged): reject collections of collections with a clear error when the schema is defined
- [melonjs/melonJS#1759](https://github.com/melonjs/melonJS/pull/1759) (merged): place tile objects on isometric maps where Tiled draws them
- [pixijs/pixijs#12324](https://github.com/pixijs/pixijs/pull/12324) (merged): add a safariFontDelay option so HTMLText can skip the fixed 100ms font wait in Safari

### Tech stack

![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Netty](https://img.shields.io/badge/Netty-0F5C8C?style=flat-square)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square)
![Windows Server](https://img.shields.io/badge/Windows%20Server-0078D6?style=flat-square)

---

## 繁體中文

### 關於我

- 專注在**線上遊戲的伺服器端**：封包協定、遊戲邏輯、經濟系統，以及營運用的管理工具
- 做即時遊戲的**連線同步**：權威伺服器、客戶端預測、延遲補償與流量優化
- 做 **2D 遊戲素材工具**：地圖、sprite、點陣字型，網頁和命令列都能用
- 處理遊戲資料用的 **MySQL／SQL Server**：結構設計、備份與效能調整

### 作品

| 專案 | 說明 |
|---|---|
| [sidescroll-net](https://github.com/vtxe02023274/sidescroll-net) | 橫向捲軸多人連線的權威伺服器：客戶端預測（修正量 0）、內插、延遲補償、快照差量與視野裁切（[線上試玩](https://vtxe02023274.github.io/sidescroll-net/)） |
| [pktspec](https://github.com/vtxe02023274/pktspec) | 用一份 YAML 描述遊戲封包，產生 Java、C#、TypeScript、C++ 讀寫程式、Wireshark 外掛與文件；`diff` 檢查新舊版相容、`fuzz` 產生測試資料 |
| [isotiles](https://github.com/vtxe02023274/isotiles) | 網頁版等角與交錯式地圖編輯器，讀寫 Tiled 地圖，渲染與 Tiled 逐像素一致（[線上試用](https://vtxe02023274.github.io/isotiles/)） |
| [aseview](https://github.com/vtxe02023274/aseview) | Aseprite 檢視與匯出：sprite sheet、逐標籤 GIF、放大、逐圖層，網頁與命令列都能用（[線上試用](https://vtxe02023274.github.io/aseview/)） |
| [fntview](https://github.com/vtxe02023274/fntview) | BMFont 點陣字型檢查與轉檔，支援 SDF／MSDF，也能從 .ttf 產生字型（[線上試用](https://vtxe02023274.github.io/fntview/)） |
| [tiledcheck](https://github.com/vtxe02023274/tiledcheck) | Tiled 地圖檢查：缺檔、超出範圍的圖塊、重疊或沒用到的 tileset，可放進 GitHub Actions |

### 開源貢獻

- [colyseus/schema#245](https://github.com/colyseus/schema/pull/245)（已合併）：多人連線狀態同步庫，巢狀集合在定義時就給出清楚的錯誤，不再到執行時才莫名失敗
- [melonjs/melonJS#1759](https://github.com/melonjs/melonJS/pull/1759)（已合併）：HTML5 遊戲引擎，等角地圖上的圖塊物件改成放在 Tiled 畫的位置，不再偏移
- [pixijs/pixijs#12324](https://github.com/pixijs/pixijs/pull/12324)（已合併）：2D 繪圖引擎，HTMLText 新增 safariFontDelay 選項，字型已載入時 Safari 不必再固定等 100ms

<div align="center">
<sub>如果有幫到你，歡迎點個星星 · If something here helps you, a star is always appreciated</sub>
</div>
