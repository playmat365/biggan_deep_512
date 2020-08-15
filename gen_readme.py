import os

root = 'pics'

def dn_sort_key(dn):
    try:
        name, _ = dn.split('_', 1)
        return int(name)
    except Exception:
        return 0

def fn_sort_key(fn):
    try:
        name, _ = fn.split('.', 1)
        return int(name)
    except Exception:
        return 0

def proc_subdir(dn, title):
    fs = []
    for fn in os.listdir(dn):
        if not fn.endswith('.jpg'):
            continue
        fs.append(fn)
    fs.sort(key=fn_sort_key)
    s = []
    for fn in fs:
        name, _ = fn.split('.')
        ds = f'![{name}]({name}.jpg)'
        s.append(ds)
    s = ' '.join(s)
    fn = os.path.join(dn, 'README.md')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(f'# {title}\n\n')
        f.write(s+'\n\n')

def main():
    fs_global = []
    dns = os.listdir(root)
    dns.sort(key=dn_sort_key)
    for dn in dns:
        if dn.startswith('.'):
            continue
        title = dn.replace('_', '-')
        dn = os.path.join(root, dn)
        if not os.path.isdir(dn):
            continue
        proc_subdir(dn, title)
        fs_global.append(f'[![{title}]({dn}/0.jpg)]({dn})')
    fn = 'README.md'
    with open(fn, 'r', encoding='utf-8') as f:
        s = f.read()
    pt = '# 预览'
    p = s.find(pt)
    if p > 0:
        s = s[:p]
    s += pt+'\n\n点击图片可查看该分类\n\n'
    s += ' '.join(fs_global)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(s+'\n\n')

if __name__ == '__main__':
    main()
