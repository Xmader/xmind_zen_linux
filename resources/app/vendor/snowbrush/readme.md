## What is Snowbrush
Snowbrush is mindmap rendering kernel of several concrete Xmind products.  
You can get an `Editor` by passing [content data](https://hq.xmind.cn:30000/seawind/seawind-node/wikis/Storage%20Specification%20GR2), and manipulate mindmap by user input(mouse or keyboard shortcut) or `Editor`'s API  
Snowbrush is reponsible for:
+ Render [XMind mindmap data](https://hq.xmind.cn:30000/seawind/seawind-node/wikis/Storage%20Specification%20GR2) using SVG
+ Workbook and Sheet manangement
+ Undo & redo
+ User interaction: drag&drop, mouse action and touch action etc.
+ Keyboard shortcut
+ API for Vana, sunlight and other MindMap application

## Dependency
+ [Backbone,js](http://backbonejs.org/)
+ [svg.js v1.0](http://svgjs.com/) (altered by ourselves)

## Directory Structure
```
|- images: icon images, such as note, label and so on.
|- js: javascript source code.
   |- core: core class and module, including `WorkbookEditor` and `SheetEditor`. **Recommend to read for everybody**
      |- action: Editor Action related source code
         |- sheetactioncreator: create sheet's actions
         |- workbookactioncreator: create workbook's actions
         |- utilcreator.js: util for action
      |- abstracteditor.js: abstract base class for SheetEditor and WorkbookEditor
      |- constant.js: All constants are defined in it
      |- events.js: helper of onEvent and onGesture API of Editor
      |- globalconfig.js: define Config Class and default configs
      |- sheeteditor.js: define SheetEditor Class, inherited from AbstractEditor
      |- WorkbookEditor.js: define WorkbookEditor Class, inherited from WorkbookEditor
   |- cssjs: css will insert into html by js, will deprecated soon
   |- lib: third-party library, may are altered by ourselves
   |- models: Model of Backbone, warper of XMind-data
   |- module: of which lifesycle is same as SheetEditor.several complex interaction including copy&paste and drag etc.
   |- render: render methods of topic and relationship etc.
   |- structures: layout strategies
   |- utils: pure and common functions
   |- view: View of Backbone, listen changing of Model, render mindmap and form a View tree of which context is SheetEditor
   |- snowbrush.js: entry of project, expose Class and functions like static namespace
|- markers: marker images
|- scripts: scripts for development and release
|- test: test data and test case
|- ui: deprecated ui source code, stay there for development convenience
|- sheeteditor.html: demo of using SheetEditor alone
|- workbookeditor.html: demo of using WorkbookEditor
```

## NPM scripts
+ `dev`: start development, build `bundle.js` and start webpack dev server
+ `start`: shortcut of `dev`
+ `test`: run mocha test case
+ `dist`: run `build` and `run-webtest-test` sequently
+ `build`: build `bundle.js`
+ `run-webtest-test`: copy resource file to `../chokit.bitbucket.io`, will deprecated soon
+ `release`: rasie version and commit
+ `build-jsdoc`: build `API.md` to `../snowbrush.wiki`
+ `edge-server`: run static dev server for edge instead of webpack-dev-server

## Installation
+ Run `npm install` at project directory
+ Copy `test\exampledata\` to `test\data\`

## Run demo
1. Run `npm start` to build `bundle.js` and setup web-server  
2. Open URL `http://127.0.0.1:8686/sheeteditor.html` or `http://127.0.0.1:8686/workbookeditor.html` on web browser

## How to import snowbrush
+ **Use [npm local path](https://docs.npmjs.com/files/package.json#local-paths)**  
  For example:
  1. Clone `snowbrush-js` in your project's parent directory
  2. Install `snowbrush-js`
  3. Write your project's `package.json` like this
  ```javascript
    {
      "name": "your project",
      "dependencies": {
        "snowbrush": "file:../snowbrush-js"
      }
    }
  ```
  4. Now you can import snowbrush like this `const snowbrush = require("snowbrush")` or `import snowbrush from "snowbrush"`
  5. **`console.log(snowbrush)` to understand its namespace!**

+ **[Submodule](https://git-scm.com/docs/git-submodule)**  
  TODO

## Getting started
`sheeteditor.html` and `workbookeditor.html` is demo. Review them to get inspiration.   
Generaly, you must do something below before create an editor:  
+ Set global config by
```
Snowbrush.config(key, value)
```
+ Fetch workbook data and sheet data which is called [content.json](https://hq.xmind.cn:30000/seawind/seawind-node/wikis/Storage%20Specification%20GR2)
+ Create `Workbook` Model and `Sheet` Model by its data
```
const sheetModel = new Snowbrush.Model.Sheet(JSON.parse(workbookData))
```
+ Get a `div` **already** mounted to DOM tree (A detached DOM may cause error)
+ Create `WorkbookEditor` by input the DOM and `Workbook` Model
+ Or create `SheetEditor` by input the DOM and `Sheet` Model
```
const se = new Snowbrush.SheetEditor({el: document.getElementById("page_content"), sheetModel: sheetModel});
se.initInnerView();
```
+ You will see XMind mindmap render inside the `div` which you pass to `Editor`.Try to manipulate it and enjoy! 

## How it work
Snowbrush will build a `Backbone.Model` tree from `content.json`, and them build related `Backbone.View` tree and render by SVG.`SheetEditor` is root `View` of inner `View`s and act as context of them.

`View` listen `Model` change by `Model`'s events, and update `View` itself.`View` and `Model` are separated totally by event and `Model` dosen't know `View`'s existence.

`View` also listen user input(mouse,touch getsture and keyboard) and manipulate `Model` directly or by `Action`(`SheetEditor`'s API)
## More
[Changelog](https://hq.xmind.cn:30000/xmind/snowbrush/wikis/changelog)  
[Code Style Stantard](https://hq.xmind.cn:30000/xmind/snowbrush/wikis/code)  
[Wiki](https://hq.xmind.cn:30000/xmind/snowbrush/wikis/Home)  
[Stroage Spec](https://hq.xmind.cn:30000/seawind/seawind-node/wikis/Storage%20Specification%20GR2)
