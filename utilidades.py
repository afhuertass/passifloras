

# utilidades


#funciones utilizadas
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly 
import plotly.plotly as py
import plotly.tools as tls

import plotly.graph_objs as go

from IPython.display import display, HTML

class analizador():

    def __init__( self , data_paths , estaciones  ,output = "."):

        # analizador de los datos.
        # inputs : data_paths, lista de los archivos de excel
        # output : una ruta donde guardar los resultados obtenidos.
        # estaciones : nombres de las estaciones agrocilmaticas
        print(data_paths)
        clima_excel = pd.read_excel( data_paths[0] , sheetname = None )
        precios_excel = pd.read_excel( data_paths[1]  , sheetname =None )
        rendimiento_excel = pd.read_excel( data_paths[2] , sheetname =None )
       
        self.rendimiento_exp = rendimiento_excel['rendimientos']
        self.rendimiento_min = rendimiento_excel['rendimiento-ministerio']
        
        
        self.brillo_solar = clima_excel['brillo_solar']
        
        self.brillo_solar.name = "Brillo Solar"
        
        self.evotransp = clima_excel['evotranspiracion']
        self.evotransp.name = "Evotranspiracion"
        
        self.humedad_relativa = clima_excel['humedad_relativa']
        self.humedad_relativa.name = "Humedad Relativa"
        
        self.estaciones = estaciones[:]

        self.df = dict()

        self.df['brillo_solar'] = self.brillo_solar
        self.df['evotransp'] = self.evotransp
        self.df['humedad_relativa'] = self.humedad_relativa
        self.df['precipitacion_max'] = clima_excel['precipitacion_maximos']
        self.df['precipitacion_num_dias'] = clima_excel['precipitacion_numero_de_dias']
        self.df['precipitacion_totales'] = clima_excel['precipitacion_totales']
        self.df['punto_de_rocio'] = clima_excel['punto_de_rocio']
        self.df['temperatura_max'] = clima_excel['temperatura_maximos']
        self.df['temperatura_medios_max'] = clima_excel['temp_medios_max']
        self.df['temperatura_medios'] = clima_excel['temp_medios']

        self.df['temperatura_medios_min'] = clima_excel['temp_medio_min']
        self.df['temperatura_min'] = clima_excel['temp_min']
        
        
       
        
        self.df['rendimiento_exp']  = self.rendimiento_exp
        self.df['rendimiento_min'] = self.rendimiento_min
        
        self.df['precios'] = precios_excel['consolidado']
        
        self.output = output

      

        self.report = '' # el reporte enpieza en blanco

        self.init_report()
        
    def init_report(self):

        self.report = """<html> 
        <head>
        <script src="https://www.w3schools.com/lib/w3data.js"></script>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <title>Reporte Interactivo </title>
        <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Bootstrap -->
        <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
        </head>
        <body>
          <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="#">Reporte </a>
        
        </div>
      </div>
    </div>
      
<div class="container">
        <h1> Analisis explotario de datos </h1>
        """
        return 
        
    def plot_save(self,  variable , estacion ,  online = False ,save = False   ):
        ss = None
        try:
        
            ss = self.df[variable ].loc[estacion]
        except:
            print("Error, no existen datos para la serie en la estacion requerida")
            return False

        ts = pd.Series( ss, index = ss.index )

        data = [ go.Scatter( x=ss.index , y = ss ) ]
        
        name = self.output + "serie_" + variable + "_ " + estacion  

        plotly_url = None 
        layout = go.Layout( title = variable , xaxis=dict( title="Tiempo", titlefont=dict( size=18)  ) , yaxis=dict(title=variable, titlefont=dict( size=18) ) )
        if online:
            fig = go.Figure( data = data , layout = layout)
            plotly_url = py.plot(fig , filename=name , auto_open=False )
            
        else:
            plotly.offline.plot( { "data": data , "layout": layout }  , filename=name , auto_open=False )
            
        
        return plotly_url
    
    def plot_many(self , variable  , estaciones , online = False , diff ='' ):
        series = []
        names = []
        name_file = 'all_{}'.format(variable)
        for estacion in estaciones:
            try :
                print(variable)
                print(estacion)
                ss = self.df[variable].loc[estacion]
            
                serie = pd.Series(ss , index = ss.index )
                series.append( serie )
                name = '{}_{}'.format( variable , estacion )
                names.append(name)
            except:
                print( "NO data para la serie")
                continue
            
        if not series :
            return False

        datas = []
        for serie, name  in zip( series , names ):

            datas.append( go.Scatter( x = serie.index , y = serie , name= name , mode='lines'  ) )
            
       
        layout = go.Layout( title = variable , xaxis=dict( title="Tiempo", titlefont=dict( size=18)  ) , yaxis=dict(title=variable, titlefont=dict( size=18) ) )
        plotly_url = None 
        if online:
            fig = go.Figure( data= datas , layout=layout )
            
            plotly_url = py.plot( fig , finename=name_file , auto_open= False )
        else:
            name_file = "./series/{}_{}.html".format(variable,estaciones[0] )
            div = plotly.offline.plot( { "data" : datas , "layout" : layout } , filename=name_file  ,  )
           
            #return plotly_url
        return plotly_url 
                
    def estadisticos(self,  variable , estacion , save = False ):

        try :

            ss = self.df[variable].loc[estacion]
        except:
            print("Error, no existen datos para la serie en la estacion requerida")
            return False

        ts = pd.Series(ss , index = ss.index )

        maxi = ts.max()
        mini = ts.min()
        moda = ts.mode()
        mediana = tf.median()
        promedio = ts.mean()

        # ya miro que hacer con esta wea

    def plot_hist(self,  variable , estaciones , bins = 20 , online = False ):

        series = []
        names = []
        try:
            for estacion in estaciones:
                ss = self.df[variable].loc[estacion].dropna().values
                series.append(ss)
                name = "hist_{}_{}".format(variable, estacion)
                names.append( name )
        except:
            print("Error, no existen datos para la serie en la estacion requerida")
            return False
        namef = "hist_{}".format( variable )
        datas = []
        for serie,name in zip( series, names ):
            maxx = np.max( serie )
            minn = np.min( serie )
            delta = (maxx - minn)/5
            hist = go.Histogram( x = serie , name=name , autobinx=False , xbins=dict( start=minn, end=maxx,size=delta )  )
            datas.append(hist )
            
        plotly_url = None
        if online:
            plotly_url = py.plot( datas , finename = namef )
        else:
            namef = "./hist/{}".format(namef)
            plotly.offline.plot( { "data": datas } , filename= namef  , auto_open = False, include_plotlyjs = False , output_type='div' )
            
        return plotly_url

    def plot_box(self,  variable , estacion , online=False):      
        try :
            data = self.df[variable].loc[ estacion ]
        except:
            print("Error, no existen datos para la serie en la estacion requerida")
            return False
        
        
        name = "{} para la estacion {}".format(variable,estacion)
        years = np.unique( data.index.year )
        years = np.char.mod('%d' , years )
        
        meses = [  '{num:02d}'.format(num=i) for i in range(1, 13) ]
        linear_data = []

        for mes in meses:

            for y in years:
                try:
                    linear_data.append( data[ y +'-'+ mes ].astype( np.float32 ).values[0] )
                except:
                    linear_data.append( np.nan )

        datos = np.array( linear_data )
        datos = datos.reshape( len(years) , len(meses) )

        df = pd.DataFrame( data = datos , columns = meses )

        datas = []

        for col in df.columns:
            print (col )
            datas.append( go.Box(y= df[col] , name = col , showlegend=False ) )
        means = df.mean()

        layout = go.Layout( title = name , xaxis=dict( title='Meses') , yaxis=dict(title=variable) )
        
        datas.append( go.Scatter( x = df.columns, y=means , mode='lines' , name='promedio' ) )
        
        
        plotly_url = None
        
        if online:
            ploty_url = py.plot( datas , filename = name )
        else:
            name = "{}_{}".format(variable , estacion)
            name = "./boxs/{}".format(name)
            plotly.offline.plot( { "data": datas , "layout":layout } , filename= name , auto_open = False   )

        return plotly_url 

    def report_block(self ,  rtype , graph_url , caption = ''):

        if rtype == 'interactive':
            graph_block = '<iframe style="border: none;" src="{graph_url}.embed" width="100%" height="600px"></iframe>'

        elif rtype == 'static':

            graph_block = (''
            '<a href="{graph_url}" target="_blank">' # Open the interactive graph when you click on the image
                '<img style="height: 400px;" src="{graph_url}.png">'
            '</a>')

        report_block = ('' +
                        graph_block + 
                        '{caption}' + # Optional caption to include below the graph
                        '<br>'      + # Line break
                        '<hr>') # horizontal line 
        
        
        return report_block.format( graph_url = graph_url , caption = caption )

    def text_block(self , text ):
        # la idea es formatear el texto en formato html para que sea cool
        
        return  "<br>" + text 
    def add_blocks(self,  variables  ,  online=False, rtype = 'interactive'  ):

        # recibir variables de interes y un caption
        # [ variable , estacion , caption ]
        
        for variable in variables:
            print ( variable[0] )
            #"21025020"
            plot_url = self.plot_save( variable[0] , variable[1] , online )
            if not plot_url:
                continue 
            _report_block = self.report_block( rtype , plot_url , variable[2] )


            self.report += _report_block

    def add_blocks_many (self , arguments ,  online , rtype = "interactive" , ty = "serie"):

        for argument in arguments:
            plot_url = None
            if ty=="serie":
                plot_url = self.plot_many( argument[0] , argument[1] , online  ) # variable, estaciones 
            elif ty=="hist":
                plot_url = self.plot_hist( argument[0] , argument[1] , online  )

            elif ty=="box":
                for estacion in argument[1]:
                    plot_url = self.plot_box( argument[0] , estacion , online )
            if not plot_url:
                continue
            _report_block = self.report_block( rtype , plot_url , argument[2])

            self.report += _report_block
            

    def report_all_clima(self , online = False ):

        keys = self.df.keys()
       
        keys.remove('precios')
        print(keys)
        arguments = []
        for key in keys:
            argument = []
            
            argument.append( key )
            argument.append( self.estaciones )
            argument.append( "" )

            arguments.append( argument )
        #print( arguments) 
        self.add_blocks_many( arguments , online , ty="serie"  )
        self.flush_report("./bootstrap/report.html")
        
    def report_all_hist_clima(self , online = False):
        keys = self.df.keys()
       
        keys.remove('precios')
        print(keys)
        arguments = []
        for key in keys:
            argument = []
            
            argument.append( key )
            argument.append( self.estaciones )
            argument.append( "" )

            arguments.append( argument )

        self.add_blocks_many( arguments , online , ty="hist"  )
        self.flush_report("./bootstrap/report.html")

    def report_all_box_clima(self , online=False ):

        keys = self.df.keys()
       
        keys.remove('precios')
        print(keys)
        arguments = []
        for key in keys:
            argument = []
            
            argument.append( key )
            argument.append( self.estaciones )
            argument.append( "" )

            arguments.append( argument )

        self.add_blocks_many( arguments , online , ty="box"  )
        self.flush_report("./bootstrap/report.html")

    def report_all_precios(self, online = False ):

        keys_pesos = [
            "agronet_bogota",
            "Corabastos",
            "agronet_bogota2",
            "Minagricultura",
            "Corabastos2",
        ]
        keys_fob = [ "Agronet1" ]
        keys_ton = [ "Agronet2" ]
        arguments = [ ["precios" , keys_pesos  , "" ]   ]
        # series de $/kig
        self.add_blocks_many( arguments , online , ty ="serie")
        # series FOB
        arguments = [ [ "precios" , keys_fob , ""] ]
        self.add_blocks_many( arguments , online , ty="serie")
        arguments = [ [ "precios" , keys_ton , ""] ]
        self.add_blocks_many( arguments , online , ty="serie")
        
    def flush_report(self, output):

        self.report += """ </div></body> </html>
        <script src="http://code.jquery.com/jquery.js"></script>
        <script src="js/bootstrap.min.js"></script> """ # closedtag
        
        with open( output , 'w') as f:
            f.write( self.report )


    def build_up_report(self ):

        box = "./boxs/"
        ser = "./series/"
        hist = "./hist/"

        self.init_report()

        series = [ f for f in os.listdir(ser) ]
        
        boxs = [ f for f in os.listdir(box ) ]
        hists = [ f for f in os.listdir(hist) ]

        self.report += "<h1> Variables de clima </h1>"
        
        for serie in series:
            # agregar al reporte
            block = "<div w3-include-html='./data/series/{}'></div>".format(serie)
            block = '<iframe style="border: none;" src="./data/series/{}" width="100%" height="600px"></iframe>'.format(serie)
            self.report += block

        self.report += "<h1> Diagramas de caja - variables de clima</h1>"
            
        for box in boxs:
            
            block = "<div w3-include-html='./data/boxs/{}'></div>".format(box)
            block = '<iframe style="border: none;" src="./data/boxs/{}" width="100%" height="600px"></iframe>'.format(box)
            self.report += block

        self.report += "<h1> Histogramas  - variables de clima</h1>"
        for hist in hists:
            
            block = "<div w3-include-html='./data/hist/{}'></div>".format(hist)
            block = '<iframe style="border: none;" src="./data/hist/{}" width="100%" height="600px"></iframe>'.format(hist)
            self.report += block

        

        self.report += """ 
        </div></body> 
        <script src="http://code.jquery.com/jquery.js"></script>
        <script src="js/bootstrap.min.js"></script> 
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <script>
        w3IncludeHTML();
        </script>
        </html>
        """ # closedtag
        
        with open( "./bootstrap/final.html" , 'w') as f:
            f.write( self.report )
