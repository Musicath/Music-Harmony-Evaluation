# 数竞考研题目分享40题

<p align="right">作者：诗弈羽弦
<p align="right">邮箱：Musicath@qq.com

## 简介

准备考研和大学生数学竞赛（非数学类）的同学们可以参与进来！

作者来自北京航空航天大学人工智能研究院，

曾获得第十二届、十三届大学生数学竞赛（非数学类）北京赛区双一等奖，

并有幸获得第十三届大学生数学竞赛（非数学类）全国总决赛资格。

由于疫情原因决赛时间有所延迟，所以一直处于低速复习阶段，

复习阶段会分享一些不错的题目并进行视频讲解。

此次分享共有$60$题，正常情况下每日更新一题。

如果想获取没有解答的单独题目，请关注微信公众号：`数学人文空间站`

如果想获取题目的讲解视频，请关注哔哩哔哩个人账号：`诗弈羽弦`

如果想和小伙伴们一起交流，请加入$QQ$讨论群：`686580713`

$$
\newcommand{\t}[0]{\times}
\newcommand{\f}[0]{\frac}
\newcommand{\dj}[0]{\Leftrightarrow}
\newcommand{\eps}[0]{\varepsilon}
\newcommand{\Ra}[0]{\Rightarrow}
\newcommand{\fd}[0]{\urcorner}
\newcommand{\balpha}[0]{\boldsymbol\alpha}
\newcommand{\bbeta}[0]{\boldsymbol\beta}
\newcommand{\bxi}[0]{\boldsymbol\xi}
\newcommand{\beps}[0]{\boldsymbol\varepsilon}
\newcommand{\tk}[0]{\_\_\_\_\_\_.}
\newcommand{\b}[1]{\boldsymbol{#1}}
\newcommand{\sm}[1]{\begin{pmatrix}#1\end{pmatrix}}
\newcommand{\mm}[1]{\begin{bmatrix}#1\end{bmatrix}}
\newcommand{\bm}[1]{\begin{Bmatrix}#1\end{Bmatrix}}
\newcommand{\vm}[1]{\begin{vmatrix}#1\end{vmatrix}}
\newcommand{\nm}[1]{\begin{Vmatrix}#1\end{Vmatrix}}
\newcommand{\ba}[1]{\begin{aligned}#1\end{aligned}}
\newcommand{\bc}[1]{\begin{cases}#1\end{cases}}
\newcommand{\df}[2]{\frac{d#1}{d#2}}
\newcommand{\pf}[2]{\frac{\part#1}{\part#2}}
$$

讲解视频链接：[诗弈羽弦数竞考研60题](https://www.bilibili.com/video/BV18S4y1s73Y?share_source=copy_web&amp;amp;vd_source=36f83685df8531da9bdca2c0ed6fea3f)


<div style="page-break-after:always"></div>

## $01-10$题


$$
\begin{align}
&(01)\int_0^{+\infty}\frac{\ln x}{x^2+a^2}dx=\tk\\\\
&(02)记D=\{(x,y)|x^2+y^2\le\pi\},\\
&\quad\quad则\iint\limits_D\left[\sin (x^2)\cos (y^2)+x\sqrt{x^2+y^2}\right]dxdy=\tk\\\\
&(03)\lim_{x\to0}\f{(1+x)^\f2x-e^2[1-\ln(1+x)]}x=\tk\\\\
&(04)\lim_{x\to0}\left(\f{1+\int_0^xe^{t^2}dt}{e^x-1}-\f1{\sin x}\right)=\tk\\\\
&(05)设f(x)在[0,+\infty)上连续可导,\\
&\quad\quad且f'(x)=\f{1}{1+f^2(x)}\left[\sqrt{\f1x}-\sqrt{\ln\left(1+\f1x\right)}\right],\\
&\quad\quad证明:\lim_{x\to+\infty}f(x)存在.\\\\
&(06)设f(x)在[0,1]上有连续导数,证明:对于x\in[0,1],有\\
&\quad\quad|f(x)|\le\int_0^1(|f(t)|+|f'(t)|)dt.\\\\
&(07)设f(x)=\int_0^x\f{\sin t}{\pi-t}dt,计算\int_0^\pi f(x)dx.\\\\
&(08)设f(x)二阶可导,且满足x=\int_0^xf(t)dt+\int_0^xtf(t-x)dt,\\
&\quad\quad求f(x)的表达式.\\\\
&(09)计算定积分I=\int_{-\pi}^{\pi}\f{x\sin x\cdot\arctan e^x}{1+\cos^2x}dx.\\\\
&(10)计算不定积分I=\int\f{x^2+1}{x^4+1}dx.
\end{align}
$$

<div style="page-break-after:always"></div>

## $11-20$题

$$
\begin{align}
&(11)求极限\lim_{x\to0}\f{\int_0^{2x}|t-x|\sin tdt}{|x|^3}.\\\\
&(12)设f(x)在[a,b]上具有连续的二阶导数,证明:存在\xi\in(a,b),使得\\
&\quad\quad\int_a^bf(x)dx=(b-a)f(\f{a+b}2)+\f1{24}(b-a)^3f''(\xi).\\\\
&(13)设F(u,v)是可微函数,证明曲面F\left(\f{x-a}{z-c},\f{y-b}{z-c}\right)=0上任一点\\
&\quad\quad处的切平面都过一定点.\\\\
&(14)设二元函数f(x,y)=|x-y|\varphi(x,y),其中\varphi(x,y)在(0,0)处连续.\\
&\quad\quad证明:f(x,y)在点(0,0)处可微分的充要条件是\varphi(0,0)=0.\\\\
&(15)求空间曲线\Gamma:\bc{x(t)=t(e^t-1)\\y(t)=t\sin t\\z(t)=t^3+t^2+1}在点P(0,0,1)处的切线.\\\\
&(16)计算\iint\limits_D\f{(x+y)\ln(1+\f yx)}{\sqrt{1-x-y}}dxdy,其中区域D由直线x+y=1与\\
&\quad\quad两坐标轴所围成的三角形区域.\\\\
&(17)设函数f(u)连续,在点u=0处可导,且f(0)=0,f'(0)=-3,求:\\
&\quad\quad\lim_{t\to0}\f1{\pi t^4}\iiint\limits_{x^2+y^2+z^2\le t^2}f(\sqrt{x^2+y^2+z^2})dxdydz.\\\\
&(18)求解微分方程:y''+y=\f1{\cos x}.\\\\
&(19)设\b A,\b B分别为m\t n,n\t m矩阵,\\
&\quad\quad求证:|\b E_m+\b A\b B|=|\b E_n+\b B\b A|.\\\\
&(20)设\b A是n阶矩阵,若存在正整数k,使得线性方程组\b A^k\b X=\b0有解向量\balpha,\\
&\quad\quad且\b A^{k-1}\balpha\neq\b0,证明:向量组\balpha,\b A\balpha,\b A^2\balpha,\cdots,\b A^{k-1}\balpha线性无关.
\end{align}
$$

<div style="page-break-after:always"></div>

## $21-30$题

$$
\begin{align}
&(21)定积分\int_1^{e^2}\f{\ln x}{\sqrt x}dx=\tk\\\\
&(22)设x\ge0,y\ge0满足x^2+y^2\le ke^{x+y},则k的取值范围为\tk\\\\
&(23)设级数\sum_{n=1}^{\infty}\f{n!}{n^n}e^{-nx}的收敛域为(a,+\infty),则a=\tk\\\\
&(24)已知矩阵\b A与\b E-\b A可逆,其中\b E为单位矩阵,若矩阵\b B满足\\
&\quad\quad(\b E-(\b E-\b A)^{-1})\b B=\b A,则\b B-\b A=\tk\\\\
&(25)设A,B,C为三个随机事件,A与B互不相容,A与C互不相容,\\
&\quad\quad B与C相互独立,且P(A)=P(B)=P(C)=\f13,\\
&\quad\quad则P(B\cup C|A\cup B\cup C)=\tk\\\\
&(26)设\bc{x=\sqrt{t^2+1}\\y=\ln(t+\sqrt{t^2+1})},则\df{^2y}{x^2}|_{t=1}=\tk\\\\
&(27)设函数f(x)满足f''(x)+af'(x)+f(x)=0(a>0),f(0)=m,\\
&\quad\quad f'(0)=n,则\int_0^{+\infty}f(x)dx=\tk\\\\
&(28)设f(x,y)=\int_0^{xy}e^{xt^2}dt,则\pf{^2f}{x\part y}|_{(1,1)}=\tk\\\\
&(29)行列式\vm{a&0&-1&1\\0&a&1&-1\\-1&1&a&0\\1&-1&0&a}=\tk\\\\
&(30)已知随机变量X服从区间(-\f{\pi}2,\f{\pi}2)上的均匀分布,Y=\sin X,\\
&\quad\quad则Cov(X,Y)=\tk
\end{align}
$$

<div style="page-break-after:always"></div>

## $31-40$题

$$
\begin{align}
&(31)设\balpha为三维单位列向量,\b E为三阶单位阵，则矩阵\b E-\balpha\balpha^T的秩为\tk\\\\
&(32)若二次曲面的方程x^2+3y^2+z^2+2axy+2xz+2yz=4,\\
&\quad\quad经过正交变换为y_1^2+4z_1^2=4,则a=\tk\\\\
&(33)设X_1,X_2,\cdots,X_n为来自正态总体N(\mu_0,\sigma^2)的简单随机样本,其中\mu_0已知,\\
&\quad\quad\sigma^2>0未知.\bar{X}和S^2分别表示样本均质和方差.\\
&\quad\quad(1)求参数\sigma^2的最大似然估计量\hat\sigma^2.\\
&\quad\quad(2)计算E(\hat \sigma^2)和D(\hat\sigma^2).\\\\
&(34)求极限\lim_{x\to0}\f1{\ln(x+\sqrt{x^2+1})}-\f1{\ln(x+1)}=\tk\\\\
&(35)设f(x)在区间[0,1]上具有连续导数,且\int_0^1x^2f'(x)dx=1,\\
&\quad\quad f(1)=\int_0^1f(x)dx.证明:存在\eta\in[0,1],s.t.f'(\eta)=-\f67.\\\\
&(36)设函数f(x)在[0,1]上具有连续导数,且\int_0^1f(x)dx=\f52,\\
&\quad\quad\int_0^1xf(x)=\f32.证明:存在\xi\in(0,1),s.t.f'(\xi)=3.\\\\
&(37)设\b A,\b B是n阶方阵,已知\b A\b B=\b A-\b B,证明:\b A\b B=\b B\b A.\\\\
&(38)设函数f(x)在区间[a,b]上连续,(a,b)内可导,且f(a)\neq f(b).\\
&\quad\quad证明:存在\xi,\eta\in(a,b),使得f'(\xi)=\f{a+b}{2\eta}f'(\eta).\\\\
&(39)设f(x)在[0,1]上连续,在(0,1)内可导且f(x)\neq0,且\lim_{x\to 0^-}\f{f(x+1)}x存在,\\
&\quad\quad证明:存在\xi\in(0,1),使得\f{1-e}{e\int_0^1f(t)dt}=-\f1{e^\xi f(\xi)}.\\\\
&(40)题接(39),证明:存在\eta\in(0,1),使得e\int_0^1f(t)dt=(e-1)e^\xi(\xi-1)f'(\eta).\\
\end{align}
$$

