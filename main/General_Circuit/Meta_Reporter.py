import yaml
import sys

def meta_report(meta_data_loc="Experiment_Data.yml"):
    """
    Reads meta data from file called "Experiment_Data.yml" and adds a report
    Parameters
    ----------
    meta_data_loc : str
        the path to file that contains experiment meta data
    Returns
    -------
    config_data : none
    """
    
    try:
        with open(meta_data_loc, "r") as stream:
            meta_data = yaml.safe_load(stream)
            report_message = report_writer(meta_data)
            f = open("Experiment_Info.txt","w" )
            f.write(report_message)
            f.close()
                
    except FileNotFoundError:
        sys.exit("File containing meta data, {}, not found. Exiting...".format(meta_data_loc))
        
def report_writer(md):
    """
    Reads meta data into function and makes txt message report.
    ----------
    md : dict
        Contains meta data from experiment file
    Returns
    -------
    message : string
        The text output for the report
    """
    s_name = md["sample_meta_data"]["sample_name"]
    s_date = md["sample_meta_data"]["sample_date"]
    s_surface = md["sample_meta_data"]["sample_surface_area"]
    imp_mode = md["experiment_meta_data"]["impedance_mode"]
    meas_volt = md["experiment_meta_data"]["measurement_voltage"]
    vs = md["experiment_meta_data"]["vs"]
    pert_v = md["experiment_meta_data"]["pertubation_voltage"]
    sf = md["experiment_meta_data"]["starting_frequency"]
    ef = md["experiment_meta_data"]["ending_frequency"]
    ppi = md["experiment_meta_data"]["points_per_interval"]
    ig = md["experiment_meta_data"]["interval_group"]
    spacing = md["experiment_meta_data"]["spacing"]
    
    intro_line = "Report for "+str(s_name)+" experiment conducted on "+str(s_date)+".\n\n"
    imp_line = "A "+str(imp_mode)+" measurement was made with a "+str(pert_v)+"mV pertubation voltage at "+str(meas_volt)+"V vs. "+str(vs)+".\n\n"
    range_line = "Experiment conducted from "+str(sf)+"Hz to "+str(ef)+"Hz with "+str(ppi)+ " points "+str(ig)+" using "+str(spacing)+" spacing.\n\n"
    surface_line = "Sample has a surface area of "+str(s_surface)+"cm^2."
    
    message = intro_line+imp_line+range_line+surface_line
    return message