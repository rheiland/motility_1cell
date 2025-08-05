# Unit test of motility

In `create_cell_types()` of `custom.cpp`, we have:
```
    std::vector<double> ctype1_direction {1.0, 0.0, 0.0};
    cell_defaults.phenotype.motility.migration_bias_direction = ctype1_direction;
```
and `config/PhysiCell_settings.xml` has:
```
                <motility>
                    <speed units="micron/min">1</speed>
                    <persistence_time units="min">0</persistence_time>
                    <migration_bias units="dimensionless">1</migration_bias>
                    <options>
                        <enabled>true</enabled>
                        <use_2D>true</use_2D>
```

We dump output to `<folder>output_1cell</folder>`

Run `make` and `project` and then:
```
~/git/motility_1cell$ python plot_xy.py 
---- for dir=  output_1cell/
t=0.0: x,y= 0.0,0.0
t=0.1: x,y= 0.15000000000000002,0.0
t=0.2: x,y= 0.25000000000000006,0.0
t=0.3: x,y= 0.3500000000000001,0.0
t=0.4: x,y= 0.4500000000000001,0.0
t=0.5: x,y= 0.55,0.0
t=0.6: x,y= 0.65,0.0
t=0.7: x,y= 0.75,0.0
t=0.8: x,y= 0.85,0.0
t=0.9: x,y= 0.95,0.0
t=1.0: x,y= 1.05,0.0
```
