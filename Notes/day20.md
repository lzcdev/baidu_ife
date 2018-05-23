[demo地址](https://lzcdev.github.io/baidu_ife/Demo/day20/spride.html)


#### JavaScript 的事件机制、事件代理
事件代理利用了冒泡原理，即子元素事件被触发的时候会一级一级的向上传播，直到触发相应父元素的事件。目的是减少dom操作，提高性能
- 不给子元素添加具体的oncilck处理方法，也能冒泡
- 子元素触发的事件冒泡会触发父元素对应的事件


[js中的事件委托或是事件代理详解](https://www.cnblogs.com/liugang-vip/p/5616484.html)

[关于JS事件冒泡与JS事件代理（事件委托](https://blog.csdn.net/supercoooooder/article/details/52190100)

#### 定时器
setTimeout()、clearTimeout()、 setInterval()、clearInterval()

用了clearInterval()，感觉不是很准确。清除的时候一定要找到那个正确的定时器

#### CSS Sprite
雪碧图？利用position计算出想要的图
