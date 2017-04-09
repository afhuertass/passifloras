

import utilidades



def arguments():
    args_desc = [ "Serie_de_datos->", "Estacion->" , "Comentarios-> "]
    informe_args = []
    end = ""
    args = []
    while end != "s":
        for i in range(0,3):
            arg = raw_input(args_desc[i])
            args.append( arg )
        informe_args.append( args )
        args = []
        end = raw_input( "Fin (s/n) --->")

    return informe_args

def arguments2():
    
    args_desc = [ "Serie_de_datos->", "Estacion->" , "Comentarios-> "]
    informe_args = []
    end = ""
    args = []
    estaciones = [] 
    while end != "s":
        
        arg = raw_input(args_desc[0])  # nombre serie
        args.append( arg )
        
        while arg != "s":
            arg = raw_input( args_desc[1])  # estacion
            estaciones.append( arg )
            arg = raw_input("Paso Siguiente?(s/n)->" )

        args.append( estaciones )
        
        arg = raw_input("Comentarios->")

        args.append( arg)
        
        informe_args.append( args )
        
        end = raw_input( "Fin (s/n) --->")

    return informe_args
    
if __name__ == "__main__":

    paths = [
        "../datos/series_consolidadas/consolidada_clima.xlsx" ,
        "../datos/series_consolidadas/consolidada_precios.xlsx" ,
        "../datos/series_consolidadas/rendimientos.xlsx"
    ]
    estaciones  =  [ "21025020" , # estacion1
                    "21035020"  , # estacion2
                     "21035040" , #estacion3
    ]
    estaciones_name = [
        "estacion1" ,
        "estacion2" ,
        "estacion3"
    ]
    estacion = "Neiva-rivera-21115040"
    analyzer = utilidades.analizador(paths , estaciones_name )

    
    #analyzer.plot_save( "brillo" , estacion )
    #analyzer.generate_report( r  )
    
    #ss = arguments()
    #print (ss) 
    #analyzer.add_blocks( ss )
    #analyzer.add_blocks_many(  ss ) 
    #analyzer.flush_report( './bootstrap/report.html')
    #analyzer.report_all_clima( online=False)
    #analyzer.report_all_hist_clima( online=False)
    #analyzer.plot_box("brillo_solar" ,"estacion2"  )
    #analyzer.report_all_box_clima( online=False)
    #analyzer.build_up_report()
    analyzer.report_all_precios()
