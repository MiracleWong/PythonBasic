# Virtualenv && VirtualenvWrapper

```
pip install virutalenv virtualenvwrapper
```

## Virtualenv的使用

### 创建环境

```
virtualenv [虚拟环境名称]
virtualenv test
```

默认创建的环境，是可以使用系统已经安装的包。

如果不想使用系统的包,加上–no-site-packeages参数

```
virtualenv --no-site-packages test
```

这个时候会创建目录test

### 激活环境

```
cd test
source ./bin/activate
```

此时，就进入了一个隔离的环境，安装，卸载和使用模块，都会在test环境中，而不会影响系统和其他环境。

### 退出环境

```
deactive
```

## VirtualenvWrapper的使用

VirtualenvWrapper可以进行环境的管理，把创建的环境记录下来，并进行管理。

### 初始化

第一次安装完成后需要，先设置一个变量WORKON_HOME，它将作为所有环境的前缀，并且source /usr/local/bin/virtualenvwrapper.sh

```
$ mkdir -p ./virtualenvs
$ export WORKON_HOME=./virtualenvs
$ source /usr/local/bin/virtualenvwrapper.sh
```

### 创建环境

```
mkvirtualenv env1
mkvirtualenv env2
```

环境创建之后，会自动进入该目录，并激活该环境。


### 切换环境

```
workon env1
workon env2
```

### 列出已有环境

```
workon
```

### 退出环境

```
deactivate
```

### 删除环境

```
rmvirtualenv env1
```