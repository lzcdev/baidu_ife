[简历地址](https://codepen.io/lzcdev/pen/GdqoRe)

选择器，还有背景，边框等一些 CSS 样式属性。

- 背景
    - background
    - background-color
    - background-image
    - background-repeat
    - background-position
- 边框 
    - border
    - border-color
    - border-style
    - border-width
    - border的上下左右
- 列表
    - list-style
    - list-style-type
    - list-style-image
- 链接
    - a:link
    - a:visited
    - a:hover
    - a:active

选择器的分组：中间用逗号隔开，会影响到所有
```css
h1,h2,h3,h4,h5,h6 {
  color: green;
  }
```

继承及其问题。根据 CSS，子元素从父元素继承属性。比如下面这个会影响到其子元素。如果想某个子元素不被父元素影响，重写一遍子元素样式即可。
```css
body {
     font-family: Verdana, sans-serif;
     }
```
由于历史原因，Netscape 4无法理解继承。所以针对它需要单独设置
```css
body  {
     font-family: Verdana, sans-serif;
}

p, td, ul, ol, li, dl, dt, dd  {
     font-family: Verdana, sans-serif;
 }
```
派生选择器通过依据元素在其位置的上下文关系来定义样式。合理地使用派生选择器，可以使 HTML 代码变得更加整洁。

比如后代选择器，会影响到儿子孙子无穷尽。后代所有的strong都会有影响。
```css
li strong {
    font-style: italic;
    font-weight: normal;
  }
```
子元素选择器，只影响到儿子。即使后代再有strong也不会影响到了。
```css
li > strong {
    font-style: italic;
    font-weight: normal;
  }
```
伪类和伪元素。伪类是一个以冒号(:)作为前缀的关键字。伪元素跟伪类很像，伪元素前缀是两个冒号 (::) 
```css
/* 伪类 */
a:visited {
  color: blue;
}
/* 伪元素 */
[href^=http]::after {
  content: '⤴';
}
```

组合选择器

| Combinators | Select  |
|:----:|:-------|:------|
|A,B|匹配满足A（和/或）B的任意元素|
|A B|匹配任意元素，满足条件：B是A的后代结点（B是A的子节点，或者A的子节点的子节点）|
|A > B|	匹配任意元素，满足条件：B是A的直接子节点|
|A + B|	匹配任意元素，满足条件：B是A的下一个兄弟节点（AB有相同的父结点，并且B紧跟在A的后面）|
|A ~ B|	匹配任意元素，满足条件：B是A之后的兄弟节点中的任意一个（AB有相同的父节点，B在A之后，但不一定是紧挨着A）|


选择器的优先级
!important > 内联样式 > ID选择器 > 类选择器> 类型选择器
注意：
- 一定要优化考虑使用样式规则的优先级来解决问题而不是 !important
- 只有在需要覆盖全站或外部 css（例如引用的 ExtJs 或者 YUI ）的特定页面中使用 !important
- 永远不要在全站范围的 css 上使用 !important
- 永远不要在你的插件中使用 !important

什么的情况下可以使用 !important：
    - 你的网站上有一个设定了全站样式的CSS文件，同时你（或是你同事）写了一些很差的内联样式。
    - #someElement p { color: blue; } p.awesome { color: red; }