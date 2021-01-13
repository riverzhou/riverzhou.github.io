# prismjs

[![Version](https://img.shields.io/npm/v/@riverzhou/prismjs)](https://www.npmjs.com/package/@riverzhou/prismjs)  [![License](https://img.shields.io/npm/l/@riverzhou/prismjs)](#)

---

 Custom PrismJS Package

## usage  

```html
<html>
  <head>
    <link rel="preload" id="prismcss" href="https://cdn.jsdelivr.net/npm/@riverzhou/prismjs/prism.min.css" as="style" onload="this.tag='loaded'" />
    <script type="text/javascript" id="prismjs" src="https://cdn.jsdelivr.net/npm/@riverzhou/prismjs/prism.min.js" charset="utf-8" async></script>
    <script>
    document.getElementById("prismjs").onload = () => {
      var prismcss = document.getElementById("prismcss");
      if (prismcss.tag == "loaded") {
        prismcss.rel = "stylesheet";
      } else {
        prismcss.onload = () => {
          this.rel = "stylesheet";
        };
      }
    };
    </script>
  </head>
</html>
```

## config

```json
{
    "themes": [
        "prism-okaidia"
    ],
    "languages": [
        "markup",
        "css",
        "clike",
        "javascript",
        "arduino",
        "bash",
        "basic",
        "c",
        "csharp",
        "cpp",
        "diff",
        "django",
        "excel-formula",
        "fortran",
        "git",
        "go",
        "http",
        "ini",
        "java",
        "json",
        "kotlin",
        "latex",
        "liquid",
        "llvm",
        "lua",
        "makefile",
        "markdown",
        "markup-templating",
        "matlab",
        "mongodb",
        "nasm",
        "nginx",
        "objectivec",
        "pascal",
        "perl",
        "php",
        "plsql",
        "properties",
        "python",
        "rest",
        "ruby",
        "scss",
        "sql",
        "swift",
        "typescript",
        "verilog",
        "vhdl",
        "vim",
        "visual-basic",
        "wasm",
        "wiki",
        "xml-doc",
        "yaml"
    ],
    "plugins": [
        "line-numbers",
        "show-language",
        "toolbar"
    ]
}
```

## lineno

```html
<body class="line-numbers"> <!-- enabled for the whole page -->
... ...
</body>
```

## code 

- Markup - `markup`, `html`, `xml`, `svg`, `mathml`, `ssml`, `atom`, `rss`
- CSS - `css`
- C-like - `clike`
- JavaScript - `javascript`, `js`
- ABAP - `abap`
- ABNF - `abnf`
- ActionScript - `actionscript`
- Ada - `ada`
- Agda - `agda`
- AL - `al`
- ANTLR4 - `antlr4`, `g4`
- Apache Configuration - `apacheconf`
- Apex - `apex`
- APL - `apl`
- AppleScript - `applescript`
- AQL - `aql`
- Arduino - `arduino`
- ARFF - `arff`
- AsciiDoc - `asciidoc`, `adoc`
- ASP.NET (C#) - `aspnet`
- 6502 Assembly - `asm6502`
- AutoHotkey - `autohotkey`
- AutoIt - `autoit`
- Bash - `bash`, `shell`
- BASIC - `basic`
- Batch - `batch`
- BBcode - `bbcode`, `shortcode`
- Birb - `birb`
- Bison - `bison`
- BNF - `bnf`, `rbnf`
- Brainfuck - `brainfuck`
- BrightScript - `brightscript`
- Bro - `bro`
- BSL (1C:Enterprise) - `bsl`, `oscript`
- C - `c`
- C# - `csharp`, `cs`, `dotnet`
- C++ - `cpp`
- CIL - `cil`
- Clojure - `clojure`
- CMake - `cmake`
- CoffeeScript - `coffeescript`, `coffee`
- Concurnas - `concurnas`, `conc`
- Content-Security-Policy - `csp`
- Crystal - `crystal`
- CSS Extras - `css-extras`
- Cypher - `cypher`
- D - `d`
- Dart - `dart`
- DataWeave - `dataweave`
- DAX - `dax`
- Dhall - `dhall`
- Diff - `diff`
- Django/Jinja2 - `django`, `jinja2`
- DNS zone file - `dns-zone-file`, `dns-zone`
- Docker - `docker`, `dockerfile`
- EBNF - `ebnf`
- EditorConfig - `editorconfig`
- Eiffel - `eiffel`
- EJS - `ejs`, `eta`
- Elixir - `elixir`
- Elm - `elm`
- Embedded Lua templating - `etlua`
- ERB - `erb`
- Erlang - `erlang`
- Excel Formula - `excel-formula`, `xlsx`, `xls`
- F# - `fsharp`
- Factor - `factor`
- Firestore security rules - `firestore-security-rules`
- Flow - `flow`
- Fortran - `fortran`
- FreeMarker Template Language - `ftl`
- GameMaker Language - `gml`, `gamemakerlanguage`
- G-code - `gcode`
- GDScript - `gdscript`
- GEDCOM - `gedcom`
- Gherkin - `gherkin`
- Git - `git`
- GLSL - `glsl`
- Go - `go`
- GraphQL - `graphql`
- Groovy - `groovy`
- Haml - `haml`
- Handlebars - `handlebars`
- Haskell - `haskell`, `hs`
- Haxe - `haxe`
- HCL - `hcl`
- HLSL - `hlsl`
- HTTP - `http`
- HTTP Public-Key-Pins - `hpkp`
- HTTP Strict-Transport-Security - `hsts`
- IchigoJam - `ichigojam`
- Icon - `icon`
- .ignore - `ignore`, `gitignore`, `hgignore`, `npmignore`
- Inform 7 - `inform7`
- Ini - `ini`
- Io - `io`
- J - `j`
- Java - `java`
- JavaDoc - `javadoc`
- JavaDoc-like - `javadoclike`
- Java stack trace - `javastacktrace`
- Jolie - `jolie`
- JQ - `jq`
- JSDoc - `jsdoc`
- JS Extras - `js-extras`
- JSON - `json`, `webmanifest`
- JSON5 - `json5`
- JSONP - `jsonp`
- JS stack trace - `jsstacktrace`
- JS Templates - `js-templates`
- Julia - `julia`
- Keyman - `keyman`
- Kotlin - `kotlin`, `kt`, `kts`
- LaTeX - `latex`, `tex`, `context`
- Latte - `latte`
- Less - `less`
- LilyPond - `lilypond`, `ly`
- Liquid - `liquid`
- Lisp - `lisp`, `emacs`, `elisp`, `emacs-lisp`
- LiveScript - `livescript`
- LLVM IR - `llvm`
- LOLCODE - `lolcode`
- Lua - `lua`
- Makefile - `makefile`
- Markdown - `markdown`, `md`
- Markup templating - `markup-templating`
- MATLAB - `matlab`
- MEL - `mel`
- Mizar - `mizar`
- MongoDB - `mongodb`
- Monkey - `monkey`
- MoonScript - `moonscript`, `moon`
- N1QL - `n1ql`
- N4JS - `n4js`, `n4jsd`
- Nand To Tetris HDL - `nand2tetris-hdl`
- Naninovel Script - `naniscript`, `nani`
- NASM - `nasm`
- NEON - `neon`
- nginx - `nginx`
- Nim - `nim`
- Nix - `nix`
- NSIS - `nsis`
- Objective-C - `objectivec`, `objc`
- OCaml - `ocaml`
- OpenCL - `opencl`
- Oz - `oz`
- PARI/GP - `parigp`
- Parser - `parser`
- Pascal - `pascal`, `objectpascal`
- Pascaligo - `pascaligo`
- PC-Axis - `pcaxis`, `px`
- PeopleCode - `peoplecode`, `pcode`
- Perl - `perl`
- PHP - `php`
- PHPDoc - `phpdoc`
- PHP Extras - `php-extras`
- PL/SQL - `plsql`
- PowerQuery - `powerquery`, `pq`, `mscript`
- PowerShell - `powershell`
- Processing - `processing`
- Prolog - `prolog`
- PromQL - `promql`
- .properties - `properties`
- Protocol Buffers - `protobuf`
- Pug - `pug`
- Puppet - `puppet`
- Pure - `pure`
- PureBasic - `purebasic`, `pbfasm`
- PureScript - `purescript`, `purs`
- Python - `python`, `py`
- Q (kdb+ database) - `q`
- QML - `qml`
- Qore - `qore`
- R - `r`
- Racket - `racket`, `rkt`
- React JSX - `jsx`
- React TSX - `tsx`
- Reason - `reason`
- Regex - `regex`
- Ren'py - `renpy`, `rpy`
- reST (reStructuredText) - `rest`
- Rip - `rip`
- Roboconf - `roboconf`
- Robot Framework - `robotframework`, `robot`
- Ruby - `ruby`, `rb`
- Rust - `rust`
- SAS - `sas`
- Sass (Sass) - `sass`
- Sass (Scss) - `scss`
- Scala - `scala`
- Scheme - `scheme`
- Shell session - `shell-session`, `sh-session`, `shellsession`
- Smali - `smali`
- Smalltalk - `smalltalk`
- Smarty - `smarty`
- SML - `sml`, `smlnj`
- Solidity (Ethereum) - `solidity`, `sol`
- Solution file - `solution-file`, `sln`
- Soy (Closure Template) - `soy`
- SPARQL - `sparql`, `rq`
- Splunk SPL - `splunk-spl`
- SQF: Status Quo Function (Arma 3) - `sqf`
- SQL - `sql`
- Stan - `stan`
- Structured Text (IEC 61131-3) - `iecst`
- Stylus - `stylus`
- Swift - `swift`
- T4 templating - `t4-templating`
- T4 Text Templates (C#) - `t4-cs`, `t4`
- T4 Text Templates (VB) - `t4-vb`
- TAP - `tap`
- Tcl - `tcl`
- Template Toolkit 2 - `tt2`
- Textile - `textile`
- TOML - `toml`
- Turtle - `turtle`, `trig`
- Twig - `twig`
- TypeScript - `typescript`, `ts`
- TypoScript - `typoscript`, `tsconfig`
- UnrealScript - `unrealscript`, `uscript`, `uc`
- V - `v`
- Vala - `vala`
- VB.Net - `vbnet`
- Velocity - `velocity`
- Verilog - `verilog`
- VHDL - `vhdl`
- vim - `vim`
- Visual Basic - `visual-basic`, `vb`, `vba`
- WarpScript - `warpscript`
- WebAssembly - `wasm`
- Wiki markup - `wiki`
- Xeora - `xeora`, `xeoracube`
- XML doc (.net) - `xml-doc`
- Xojo (REALbasic) - `xojo`
- XQuery - `xquery`
- YAML - `yaml`, `yml`
- YANG - `yang`
- Zig - `zig`

