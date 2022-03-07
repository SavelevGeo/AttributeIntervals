# AttributeIntervals
A yet unpublished [QGIS](https://www.qgis.org/en/site/) plugin to detect intervals of consecutive values

It analizes an text or number attribute of selected features in input layer and rearranges its data into series of continious intervals

An example result

```
5 intervals in Names:
3295 - 3302, 3318 - 3319, 3327 - 3331, 3344 - 3347, 3349 - 3350
```

![example](https://user-images.githubusercontent.com/57714410/157022239-18dbbb87-6afc-44d7-a846-d1722dc663cc.png)


# Install
Copy the `AttributeIntervals` folder to your QGIS profile python plugins folder e.g. `default/python/plugins`

Activate it in the `Plugins` > `Manage and Install Plugins...` window
![activation](https://user-images.githubusercontent.com/57714410/157021504-c0b1c335-ab44-411b-8598-8d3cb957e8e3.png)

# Get a point layer and open the plugin dock
As an example you cand use a set of photos and add it via `Processing toolbox` > `Vector creation` > `Import geotagged photos`

![start](https://user-images.githubusercontent.com/57714410/157023997-4a7e7177-4fc7-442b-984f-cd692aa94080.png)

Choose the `field` you need, to use a prefix press `Get value` and edit it so you get a repeating value, press `Calculate intervals`

![calculation](https://user-images.githubusercontent.com/57714410/157025095-12d8464a-6bc0-477c-acc1-9115ccd9a850.png)
