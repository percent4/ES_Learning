> 本文将详细介绍Kibana中的可视化数据分析功能。

**ElasticSearch**不仅提供了搜索功能，还能进行数据分析。而**Kibana**是**ElasticSearch**的可视化工具，提供了众多高级、好用的功能，其中之一便是可视化数据分析功能。

在文章[NLP（八十一）智能文档问答助手项目改进](https://mp.weixin.qq.com/s?__biz=MzU2NTYyMDk5MQ==&mid=2247486103&idx=1&sn=caa204eda0760bab69b7e40abff8e696&chksm=fcb9b307cbce3a1108d305ec44281e3446241e90e9c17d62dd0b6eaa48cba5e20d31f0129584&token=537956206&lang=zh_CN#rd)中，笔者介绍了在项目中已经使用到了可视化数据分析功能，因此，本文的示例数据即为**智能文档问答助手项目**中的数据。

本文将详细介绍如何在Kibana中使用可视化数据分析功能。

## 准备

首先，本文中使用的**ElasticSearch**与**Kibana**工具的版本号为7.17.0，采用Docker容器化部署在本地。

**ElasticSearch**中使用的index为`docs`，该index共有249个文档，其mapping如下：

```json
{
  "docs" : {
    "mappings" : {
      "properties" : {
        "cont_id" : {
          "type" : "integer"
        },
        "content" : {
          "type" : "text",
          "analyzer" : "ik_smart"
        },
        "file_type" : {
          "type" : "keyword"
        },
        "insert_time" : {
          "type" : "date",
          "format" : "yyyy-MM-dd HH:mm:ss"
        },
        "source" : {
          "type" : "text",
          "fields" : {
            "keyword" : {
              "type" : "keyword",
              "ignore_above" : 256
            }
          }
        }
      }
    }
  }
}
```

`cont_id`为划分后的chunk在原文中的序号，`content`为划分后的chunk内容，`file_type`为文档类型，共有txt, docx, pdf, string, url五种，`insert_time`为插入时间，`source`为chunk的来源。

## 数据分析

### Index管理

在Kibana左侧，选择Stack Management -> Index Management，即可查看index情况：

![Kibana中的索引管理](https://s2.loli.net/2023/12/22/yM4ckaRlGtqzve3.png)

在Index Patterns中点击docs这个索引，即可查看该索引中的字段：

![docs*索引中的字段详情](https://s2.loli.net/2023/12/22/7bRt34quTiSOK8H.png)

### Discover

在Kibana左侧，选择Home -> Analytics -> Discover，再选择index为docs*，在Available fields中对cont_id, content, file_type, insert_time, source五个字段点击+号，就能查看这些字段的数据，如下图：

![全量数据查看](https://s2.loli.net/2023/12/22/NbAkoVsWhTPwO1e.png)

在上方的Search栏中，可进行条件筛选，我们去file_type为pdf的数据进行查看，命令为

> file_type : "pdf" 

数据如下图所示：


![筛选后数据查看](https://s2.loli.net/2023/12/22/2kTnOrjt8ozlf3q.png)

Search栏还支持更高级的搜索条件，可使用KQL(Kibana Query Language)轻松进行查询。

## 图表

Kibana除了能够支持数据的可视化管理和开发调试之外，还支持用统计图表对索引数据进行可视化分析。你不需要写任何代码，直接在Kibana中使用现有的控件就能制作出各式各样的统计图表用于页面展示，比如折线图、直方图、饼图等。

点击 Analytics -> Dashboard -> Create new dashboard, 选择Create visualization, 在左侧选择index模式为docs，就能看到可分析的字段，如下：

![可用于分析的字段](https://s2.loli.net/2023/12/22/29MOJglNPyWXErd.png)

> 注意，text类型的字段不支持可视化分析。

### Table

点击file_type字段，即可看到数据统计信息，如下：

![file_type字段统计信息](https://s2.loli.net/2023/12/22/c71j9s4iglZGNFx.png)

点击 + 号，在相邻的右上方选择Table，即可查看file_type各个取值的计数，如下：

![每种文件类型的chunk数据表格](https://s2.loli.net/2023/12/21/gSIFsClVfYJjch6.png)

此时，在右边，Table栏下的Metrics已自动设置为Count of records(计数)，如下：

![图表设置项](https://s2.loli.net/2023/12/22/mJS7tRCq5c8nj94.png)

可对Metrics再进行设置，比如修改列名，在Display name中修改即可，还能设置文本对齐方式，是否隐藏列等功能。

![设置详情](https://s2.loli.net/2023/12/22/iGuRIUZcoMwyOek.png)

对Metrics设置项，选择Unique count, 字段选择source，即可统计不同文本类型的对应文件数量，如下：

![每种文件类型的文件数量表格](https://s2.loli.net/2023/12/22/N74Am6lX58F1ISY.png)

## 横向、纵向柱状图

柱状图需要设置横轴（X）与纵轴（Y），字段选取file_type，绘制不同文件类型对应的chunk数量。

选择纵向柱状图（Bar vertical），横轴为Top values of file_type，纵轴为Count of records，绘制的纵向柱状图如下：

![每种文件类型的chunk纵向柱状图](https://s2.loli.net/2023/12/21/cXIglSrNWubDQwn.png)

在图标栏选择横向柱状图（Bar Horizontal）,即可切换为横向柱状图，如下：

![每种文件类型的chunk横向柱状图](https://s2.loli.net/2023/12/22/ZMyL9Vrjp36oOqv.png)

## 饼图

饼图的绘制类似于柱状图，选择字段为file_type即可，Size by选择Count of records，如下：

![每种文件类型的chunk饼图](https://s2.loli.net/2023/12/21/kTY2mP6vcr5DKax.png)

## 折线图

折线图（Line）的绘制类似于柱状图，横轴为insert_time，纵轴为Count of records, 得到不同时间段的插入的chunk数量的折线图如下：

![文件插入时间与chunk数量的折线图](https://s2.loli.net/2023/12/21/d9IJatvEYi7P38W.png)

> 注意，需要在上方的日历图标选择对应的时间段。重点需要注意的是，Kibana中的时间可能与ES中的时间字段取值可能有时区差，需留心，比如笔者在Kinana中的insert_time与ES中的insert_time就有时差，相差8个小时。

Kibana还支持更多的图表类型，随着版本的更新，支持的图标类型会更丰富，笔者在这里不再一一赘述。

## Canvas（画布）

Canvas画布可以创建一系列的可视化展示页面以呈现各种分析图表，还可以使用图片、文本框等组件图文并茂地展示数据。Canvas画布还可以自动播放，其效果有点类似PPT，你可以设置每个Canvas画布页面的轮播时间间隔。

笔者创建的Canvas例子如下：

![示例Canvas](https://s2.loli.net/2023/12/22/fRLVJ1NOInwpSWy.png)

## 总结

本文主要介绍了笔者在日常工作项目中会用到的Kibana可视化数据分析功能，主要介绍了Kibana的Index管理、统计图表绘制、Canvas绘制等。