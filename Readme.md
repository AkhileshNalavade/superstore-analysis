AttributeError                            Traceback (most recent call last)
Cell In[14], line 7
      4 sns.set_style("whitegrid")
      6 plt.figure(figsize=(7,5))
----> 7 sns.lineplot(x=monthly_sales.index.astype(str),
      8              y=monthly_sales.values,
      9              market ='o')
     10 plt.title("Monthly Sales Trend")
     11 plt.xlabel("Month")

File c:\Users\USER\anaconda3\Lib\site-packages\seaborn\relational.py:645, in lineplot(data, x, y, hue, size, style, units, palette, hue_order, hue_norm, sizes, size_order, size_norm, dashes, markers, style_order, estimator, errorbar, n_boot, seed, orient, sort, err_style, err_kws, legend, ci, ax, **kwargs)
    642 color = kwargs.pop("color", kwargs.pop("c", None))
    643 kwargs["color"] = _default_color(ax.plot, hue, color, kwargs)
--> 645 p.plot(ax, kwargs)
    646 return ax

File c:\Users\USER\anaconda3\Lib\site-packages\seaborn\relational.py:459, in _LinePlotter.plot(self, ax, kws)
    457         lines.extend(ax.plot(unit_data["x"], unit_data["y"], **kws))
    458 else:
--> 459     lines = ax.plot(sub_data["x"], sub_data["y"], **kws)
    461 for line in lines:
    463     if "hue" in sub_vars:

File c:\Users\USER\anaconda3\Lib\site-packages\matplotlib\axes\_axes.py:1721, in Axes.plot(self, scalex, scaley, data, *args, **kwargs)
...
   1194                     errfmt.format(cls=type(self), prop_name=k))
   1195             ret.append(func(v))
   1196 if ret:

AttributeError: Line2D.set() got an unexpected keyword argument 'market'