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
Describe game packets once in YAML, including bit fields and conditional fields, then generate encoders and decoders for Java, C#, TypeScript and C++, a Wireshark dissector and a reference document. `diff` flags changes that break old clients and `fuzz` writes test corpora.

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
- [melonjs/melonJS#1766](https://github.com/melonjs/melonJS/pull/1766) (merged): project isometric collision shapes with the map tile ratio instead of a fixed 2:1
- [diasurgical/DevilutionX#8808](https://github.com/diasurgical/DevilutionX/pull/8808) (merged): fix the build with UNPACKED_MPQS=ON by always including the mod identity header
- [adamhathcock/sharpcompress#1497](https://github.com/adamhathcock/sharpcompress/pull/1497) (merged): flush the final block when a DeflateStream is disposed with leaveOpen: true
- [fallahn/tmxlite#187](https://github.com/fallahn/tmxlite/pull/187) (merged): resolve tileset and template paths relative to their own file so templates in subfolders load
- [philterd/phileas-dotnet#200](https://github.com/philterd/phileas-dotnet/pull/200) (merged): stop the ZIP code filter from flagging five digits hyphen-joined to a longer identifier such as `2026-00847`
- [mini-software/MiniExcel#1052](https://github.com/mini-software/MiniExcel/pull/1052) (merged): honor ReadEmptyFieldsAsDefault for CSV files read with a header row
- [MapsterMapper/Mapster#1036](https://github.com/MapsterMapper/Mapster/pull/1036) (merged): escape control characters in char and string constants so translated expressions and generated code compile
- [RevenantX/LiteNetLib#621](https://github.com/RevenantX/LiteNetLib/pull/621) (merged): cut strings before a surrogate pair when truncating to maxLength so NetDataWriter no longer throws on emoji at the limit
- [ncalc/ncalc#645](https://github.com/ncalc/ncalc/pull/645) (merged): keep Guid values in ToExpressionString output instead of dropping them
- [quartznet/quartznet#4363](https://github.com/quartznet/quartznet/pull/4363) (merged): a calendar with no base calendar no longer equals the same calendar layered over one, making the six calendar Equals symmetric
- [NLog/NLog#6380](https://github.com/NLog/NLog/pull/6380) (merged): parse integer literals outside the Int32 range in conditions instead of throwing OverflowException
- [mini-software/MiniExcel#1059](https://github.com/mini-software/MiniExcel/pull/1059) (merged): strip enclosing quotes before unescaping CSV fields so fields made only of quotes round-trip

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
| [pktspec](https://github.com/vtxe02023274/pktspec) | 用一份 YAML 描述遊戲封包（支援位元欄位與條件欄位），產生 Java、C#、TypeScript、C++ 讀寫程式、Wireshark 外掛與文件；`diff` 檢查新舊版相容、`fuzz` 產生測試資料 |
| [isotiles](https://github.com/vtxe02023274/isotiles) | 網頁版等角與交錯式地圖編輯器，讀寫 Tiled 地圖，渲染與 Tiled 逐像素一致（[線上試用](https://vtxe02023274.github.io/isotiles/)） |
| [aseview](https://github.com/vtxe02023274/aseview) | Aseprite 檢視與匯出：sprite sheet、逐標籤 GIF、放大、逐圖層，網頁與命令列都能用（[線上試用](https://vtxe02023274.github.io/aseview/)） |
| [fntview](https://github.com/vtxe02023274/fntview) | BMFont 點陣字型檢查與轉檔，支援 SDF／MSDF，也能從 .ttf 產生字型（[線上試用](https://vtxe02023274.github.io/fntview/)） |
| [tiledcheck](https://github.com/vtxe02023274/tiledcheck) | Tiled 地圖檢查：缺檔、超出範圍的圖塊、重疊或沒用到的 tileset，可放進 GitHub Actions |

### 開源貢獻

- [colyseus/schema#245](https://github.com/colyseus/schema/pull/245)（已合併）：多人連線狀態同步庫，巢狀集合在定義時就給出清楚的錯誤，不再到執行時才莫名失敗
- [melonjs/melonJS#1759](https://github.com/melonjs/melonJS/pull/1759)（已合併）：HTML5 遊戲引擎，等角地圖上的圖塊物件改成放在 Tiled 畫的位置，不再偏移
- [pixijs/pixijs#12324](https://github.com/pixijs/pixijs/pull/12324)（已合併）：2D 繪圖引擎，HTMLText 新增 safariFontDelay 選項，字型已載入時 Safari 不必再固定等 100ms
- [melonjs/melonJS#1766](https://github.com/melonjs/melonJS/pull/1766)（已合併）：HTML5 遊戲引擎，等角地圖的碰撞形狀依圖塊比例投影，非 2:1 圖塊不再左右拉伸
- [diasurgical/DevilutionX#8808](https://github.com/diasurgical/DevilutionX/pull/8808)（已合併）：經典 ARPG 的開源移植，開啟 UNPACKED_MPQS 時一律引入 mod 標頭檔，修好編譯失敗
- [adamhathcock/sharpcompress#1497](https://github.com/adamhathcock/sharpcompress/pull/1497)（已合併）：.NET 壓縮函式庫，DeflateStream 以 leaveOpen: true 關閉時補寫最後的壓縮區塊，不再輸出空資料
- [fallahn/tmxlite#187](https://github.com/fallahn/tmxlite/pull/187)（已合併）：C++ Tiled 地圖讀取庫，物件範本與其圖塊集改從各自所在目錄解析路徑，放在子資料夾的範本不再讀不到
- [philterd/phileas-dotnet#200](https://github.com/philterd/phileas-dotnet/pull/200)（已合併）：.NET 個資遮蔽函式庫，郵遞區號過濾器不再把 `2026-00847` 這類用連字號接在較長編號後的五位數誤判為郵遞區號
- [mini-software/MiniExcel#1052](https://github.com/mini-software/MiniExcel/pull/1052)（已合併）：.NET Excel／CSV 讀寫庫，有標題列的 CSV 也套用 ReadEmptyFieldsAsDefault，空欄位改回型別預設值
- [MapsterMapper/Mapster#1036](https://github.com/MapsterMapper/Mapster/pull/1036)（已合併）：.NET 物件對應庫，運算式轉成 C# 程式碼時跳脫字元與字串常數裡的換行等控制字元，產生的程式碼不再無法編譯
- [RevenantX/LiteNetLib#621](https://github.com/RevenantX/LiteNetLib/pull/621)（已合併）：C# 可靠 UDP 網路庫，字串依 maxLength 截斷時不再切開代理字元對，長度上限處有 emoji 的訊息不再送出失敗
- [ncalc/ncalc#645](https://github.com/ncalc/ncalc/pull/645)（已合併）：.NET 運算式求值庫，ToExpressionString 輸出時保留 Guid 值，不再被吞掉變成空字串
- [quartznet/quartznet#4363](https://github.com/quartznet/quartznet/pull/4363)（已合併）：.NET 排程函式庫，沒有基底的行事曆不再等於套了基底的同一份行事曆，六種行事曆的 Equals 改為對稱
- [NLog/NLog#6380](https://github.com/NLog/NLog/pull/6380)（已合併）：.NET 日誌函式庫，條件式裡超出 Int32 範圍的整數改為正常解析，不再丟出 OverflowException
- [mini-software/MiniExcel#1059](https://github.com/mini-software/MiniExcel/pull/1059)（已合併）：.NET Excel／CSV 讀寫庫，CSV 欄位先去掉外層引號再還原跳脫，全是引號的欄位不再少一個引號

<div align="center">
<sub>如果有幫到你，歡迎點個星星 · If something here helps you, a star is always appreciated</sub>
</div>
