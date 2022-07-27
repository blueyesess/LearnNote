AXI4
========

AXI4（Advanced eXtensible Interface）由 ARM 公司提出一种面向高性能、高带宽、低延迟的片内总线。

优势

- 适合高带宽、低延迟应用，如：高速存储外设 DDR4
- 可灵活拓展总线位宽以及功能，如 ACE 就是基于 AXI 拓展
- 标准化通用总线，Xilinx 所有 ip 都支持 AXI

总线特点

- 控制/数据通道分离
- 读/写通道分离（减少 DMA 的代价）
- 支持地址非对齐传输，具备突发传输且仅需指定开始地址（区别 AHB）
- 支持发出多个未完成的地址（outstanding addresses ）
- 支持乱序事务（transaction）传输
- 允许添加寄存器打拍来保证时序收敛

概念
^^^^^^^^^^

版本差异
^^^^^^^^^

====  ====
版本  描述
====  ====
AXI3  初版
AXI4  取消 WID，不再支持写乱序、交织 
     
      AxLOCK 改为 1-bit，取消 LOCK 信号，只支持独占访问
     
      增加信号 AxQOS，AxREGION，AxUSER
AXI5  在 AXI4 基础上，增加额外特性信号
====  ====




