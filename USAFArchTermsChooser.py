import streamlit as st
from st_copy import copy_button
import re

finalString = ""
finalMatsString = ""
finalTimeString = ""

st.title("USAF Architectural Terms Chooser")

st.subheader("Facility Type")
with st.expander("Facility Type", expanded = False):
    with st.expander("Administration:", expanded = False):
        terms1 = st.multiselect("Choose all that apply:", ["Administration", "Command Facility", "Communications Center", "Technical/Professional Library", "Recruit Processing", "Legal Facility", "Review Stand/Grandstand"])
        selectionText1 = ";".join(terms1)
        finalString += selectionText1

        if "Administration" in terms1:
            with st.expander("Administrative Buildings", expanded = True):
                terms1dot1 = st.multiselect("Choose all that apply:", ["Administration Building", "Administration Facility", "Administrative Building", "Administrative Structure", "Housing Management"])
                selectionText1dot1 = ";".join(terms1dot1)
                finalString += ";" + selectionText1dot1 + ";"

        if "Command Facility" in terms1:
            with st.expander("Command Facilities", expanded = True):
                terms1dot2 = st.multiselect("Choose all that apply:", ["Headquarters", "Command Building", "Command Center", "Logistics Facility"])
                selectionText1dot2 = ";".join(terms1dot2)
                finalString += ";" + selectionText1dot2 + ";"

        if "Technical/Professional Library" in terms1:
            with st.expander("Technical/Professional Library", expanded = True):
                terms1dot3 = st.multiselect("Choose all that apply:", ["Technical Library", "Professional Library"])
                selectionText1dot3 = ";".join(terms1dot3)
                finalString += ";" + selectionText1dot3 + ";"

        if "Legal Facility" in terms1:
            with st.expander("Legal Facility", expanded = True):
                terms1dot4 = st.multiselect("Choose all that apply:", ["Defense Counsel", "Law Center"])
                selectionText1dot4 = ";".join(terms1dot4)
                finalString += ";" + selectionText1dot4 + ";"


    with st.expander("Airfield/Aircraft:", expanded = False):
        terms2 = st.multiselect("Choose all that apply:", ["Airfield Pavement", "Aircraft Support", "Control Tower", "Hangar", "Radar Pad"])
        selectionText2 = ";".join(terms2)
        finalString += selectionText2

        if "Airfield Pavement" in terms2:
            with st.expander("Airfield Pavement", expanded = True):
                terms2dot1 = st.multiselect("Choose all that apply:", ["Runway", "Taxiway", "Landing Pad", "Takeoff Pad", "Helicopter Pad", "Helicopter Landing Zone", "Aircraft Apron", "Arming Pad", "Disarming Pad", "Cargo Load Area", "Cargo Loading", "Cargo Loading Facility", "Cargo Unload Area", "Cargo Unloading", "Cargo Unloading Facility"])
                selectionText2dot1 = ";".join(terms2dot1)
                finalString += ";" + selectionText2dot1 + ";"

        if "Aircraft Support" in terms2:
            with st.expander("Aircraft Support", expanded = True):
                terms2dot2 = st.multiselect("Choose all that apply:", ["Aircraft Support Facility", "Aircraft Support Building", "Aircraft Support Structure"])
                selectionText2dot2 = ";".join(terms2dot2)
                finalString += ";" + selectionText2dot2 + ";"


    with st.expander("Cemetery, Memorial, Monument, Museum:", expanded = False):
        terms3 = st.multiselect("Choose all that apply:", ["Museum", "Monument", "Cemetery"])
        selectionText3 = ";".join(terms3)
        finalString += selectionText3

        if "Museum" in terms3:
            with st.expander("Museum", expanded = True):
                terms3dot1 = st.multiselect("Choose all that apply:", ["Heritage Center", "Exhibit Facility"])
                selectionText3dot1 = ";".join(terms3dot1)
                finalString += ";" + selectionText3dot1 + ";"

        if "Monument" in terms3:
            with st.expander("Monument", expanded = True):
                terms3dot2 = st.multiselect("Choose:", ["Memorial"])
                selectionText3dot2 = ";".join(terms3dot2)
                finalString += ";" + selectionText3dot2 + ";"

        if "Cemetery" in terms3:
            with st.expander("Cemetery", expanded = True):
                terms3dot3 = st.multiselect("Choose all that apply:", ["Columbarium", "Pet Cemetery"])
                selectionText3dot3 = ";".join(terms3dot3)
                finalString += ";" + selectionText3dot3 + ";"


    with st.expander("Communications/Navigation:", expanded = False):
        terms4 = st.multiselect("Choose all that apply:", ["Communications Facility", "Navigation Facility", "Weather/Meteorological Facility"])
        selectionText4 = ";".join(terms4)
        finalString += selectionText4

        if "Communications Facility" in terms4:
            with st.expander("Communications Facility", expanded = True):
                terms4dot1 = st.multiselect("Choose all that apply:", ["Communications Building", "Communications Tower", "Communications Lines", "Communications Cabling", "Communications Fiber"])
                selectionText4dot1 = ";".join(terms4dot1)
                finalString += ";" + selectionText4dot1 + ";"

        if "Navigation Facility" in terms4:
            with st.expander("Navigation Facility", expanded = True):
                terms4dot2 = st.multiselect("Choose all that apply:", ["Navigation Building", "Navigation Structure", "Airfield Lighting", "Airfield Sign", "Airfield Marker", "Obstruction Lighting", "Beacon", "Instrument Landing System"])
                selectionText4dot2 = ";".join(terms4dot2)
                finalString += ";" + selectionText4dot2 + ";"

        if "Weather/Meteorological Facility" in terms4:
            with st.expander("Weather/Meteorological Facility", expanded = True):
                terms4dot3 = st.multiselect("Choose all that apply:", ["Weather Building", "Weather Facility", "Weather Structure", "Meteorological Building", "Meteorological Facility", "Meteorological Structure", "Meteorological System"])
                selectionText4dot3 = ";".join(terms4dot3)
                finalString += ";" + selectionText4dot3 + ";"


    with st.expander("Fueling/Fuel Storage:", expanded = False):
        terms5 = st.multiselect("Choose all that apply:", ["Fueling Facility", "Defueling Facility", "Fuel Storage Facility"])
        selectionText5 = ";".join(terms5)
        finalString += selectionText5

        if "Fueling Facility" in terms5:
            with st.expander("Fueling Facility", expanded = True):
                terms5dot1 = st.multiselect("Choose all that apply:", ["Fueling Station", "FuelingFacility", "Fueling System", "Fueling Pit", "Fuel Dispensing System", "Fuel Dispensing Pit", "Fuel Storage", "Fuel Tank", "Fuel Pump", "Fuel Pump Station", "Liquid Fuel Loading"])
                selectionText5dot1 = ";".join(terms5dot1)
                finalString += ";" + selectionText5dot1 + ";"

        if "Defueling Facility" in terms5:
            with st.expander("Defueling Facility", expanded = True):
                terms5dot2 = st.multiselect("Choose all that apply:", ["Defueling System", "Defueling Pit", "Liquid Fuel Unloading"])
                selectionText5dot2 = ";".join(terms5dot2)
                finalString += ";" + selectionText5dot2 + ";"

        if "Fuel Storage Facility" in terms5:
            with st.expander("Fuel Storage Facility", expanded = True):
                terms5dot3 = st.multiselect("Choose all that apply:", ["Petroleum Storage Tank", "Rocket Propellant Storage Tank"])
                selectionText5dot3 = ";".join(terms5dot3)
                finalString += ";" + selectionText5dot3 + ";" 


    with st.expander("Hazardous and General Storage:", expanded = False):
        terms6 = st.multiselect("Choose all that apply:", ["Hazardous Liquid Storage", "Hazardous Materials Storage", "Arsenal Storage"])
        selectionText6 = ";".join(terms6)
        finalString += selectionText6

        if "Hazardous Liquid Storage" in terms6:
            with st.expander("Hazardous Liquid Storage", expanded = True):
                terms6dot1 = st.multiselect("Choose all that apply:", ["Fuel Storage", "Fuel Tank", "Bulk Liquid Storage", "Bulk Liquid Tank", "Liquid Oxygen Storage", "Rocket Propellant Storage", "Liquid Propellant Storage"])
                selectionText6dot1 = ";".join(terms6dot1)
                finalString += ";" + selectionText6dot1 + ";"

        if "Hazardous Materials Storage" in terms6:
            with st.expander("Hazardous Materials Storage", expanded = True):
                terms6dot2 = st.multiselect("Choose all that apply:", ["Hazardous Materials Depot"])
                selectionText6dot2 = ";".join(terms6dot2)
                finalString += ";" + selectionText6dot2 + ";"

        if "Arsenal Storage" in terms6:
            with st.expander("Arsenal Storage", expanded = True):
                terms6dot3 = st.multiselect("Choose all that apply:", ["Ammunition Storage", "Ammunition Depot", "Ammunition Arsenal", "Ammunition Shed", "Ammunition Igloo", "High Explosive Magazine", "Missile Storage Facility", "Missile Storage Igloo", "Missile Silo", "Arms Storage", "Open Storage"])
                selectionText6dot3 = ";".join(terms6dot3)
                finalString += ";" + selectionText6dot3 + ";"            


    with st.expander("Housing:", expanded = False):
        terms7 = st.multiselect("Choose all that apply:", ["Family Housing", "Unaccompanied Personnel Housing", "Dining Facility", "Latrine/Shower", "Camp"])
        selectionText7 = ";".join(terms7)
        finalString += selectionText7

        if "Family Housing" in terms7:
            with st.expander("Family Housing", expanded = True):
                terms7dot1 = st.multiselect("Choose all that apply:", ["Family Quarters", "Dwelling", "Garage", "Carport", "Housing Support Facility"])
                selectionText7dot1 = ";".join(terms7dot1)
                finalString += ";" + selectionText7dot1 + ";"

        if "Unaccompanied Personnel Housing" in terms7:
            with st.expander("Unaccompanied Personnel Housing", expanded = True):
                terms7dot2 = st.multiselect("Choose all that apply:", ["UPH", "Barracks", "Dormitory", "Garage"])
                selectionText7dot2 = ";".join(terms7dot2)
                finalString += ";" + selectionText7dot2 + ";"

        if "Dining Facility" in terms7:
            with st.expander("Dining Facility", expanded = True):
                terms7dot3 = st.multiselect("Choose all that apply:", ["Flight Kitchen", "Food Service"])
                selectionText7dot3 = ";".join(terms7dot3)
                finalString += ";" + selectionText7dot3 + ";"

        if "Latrine/Shower" in terms7:
            with st.expander("Latrine/Shower", expanded = True):
                terms7dot4 = st.multiselect("Choose all that apply:", ["Shower Facility", "Sanitary Latrine"])
                selectionText7dot4 = ";".join(terms7dot4)
                finalString += ";" + selectionText7dot4 + ";"

        if "Camp" in terms7:
            with st.expander("Camp", expanded = True):
                terms7dot5 = st.multiselect("Choose:", ["Tent Pad"])
                selectionText7dot5 = ";".join(terms7dot5)
                finalString += ";" + selectionText7dot5 + ";"


    with st.expander("Installation/Community Support:", expanded = False):
        terms8 = st.multiselect("Choose all that apply:", ["Emergency/Security Facility", "Shelter", "Commercial/Retail", "Child/Youth Services", "Church/Chapel", "Lodging", "Recreation"])
        selectionText8 = ";".join(terms8)
        finalString += selectionText8

        if "Emergency/Security Facility" in terms8:
            with st.expander("Emergency/Security Facility", expanded = True):
                terms8dot1 = st.multiselect("Choose all that apply:", ["Fire Station", "Police Station", "Prison/Confinement/Correction Facility", "Visitor Control Center"])
                selectionText8dot1 = ";".join(terms8dot1)
                finalString += ";" + selectionText8dot1 + ";"

        if "Shelter" in terms8:
            with st.expander("Shelter", expanded = True):
                terms8dot2 = st.multiselect("Choose all that apply:", ["Smoke Shelter", "Bus Station", "Bus Shelter", "Air Raid Shelter", "Fallout Shelter", "Storm Shelter"])
                selectionText8dot2 = ";".join(terms8dot2)
                finalString += ";" + selectionText8dot2 + ";"

        if "Commercial/Retail" in terms8:
            with st.expander("Commercial/Retail", expanded = True):
                terms8dot3 = st.multiselect("Choose all that apply:", ["Restaurant", "Exchange Facility", "Thrift Shop", "Laundry/Dry Cleaning Facility", "Bank/Credit Union", "Car Wash Facility/Structure", "Commissary"])
                selectionText8dot3 = ";".join(terms8dot3)
                finalString += ";" + selectionText8dot3 + ";"

        if "Child/Youth Services" in terms8:
            with st.expander("Child/Youth Services", expanded = True):
                terms8dot4 = st.multiselect("Choose all that apply:", ["Education Center/Facility", "School (Public)", "Nursery/Child Care/Youth Care Facility"])
                selectionText8dot4 = ";".join(terms8dot4)
                finalString += ";" + selectionText8dot4 + ";"

        if "Lodging" in terms8:
            with st.expander("Lodging", expanded = True):
                terms8dot5 = st.multiselect("Choose:", ["Hotel"])
                selectionText8dot5 = ";".join(terms8dot5)
                finalString += ";" + selectionText8dot5 + ";"

        if "Recreation" in terms8:
            with st.expander("Recreation", expanded = True):
                terms8dot6 = st.multiselect("Choose all that apply:", ["Athletic Building", "Athletic Structure", "Athletic Field", "Stable/Paddock/Corral", "Boathouse", "Craft Center", "Golf Club House/Course", "Theater/Auditorium", "Bowling Alley", "Open Mess/Club Facility", "Library"])
                selectionText8dot6 = ";".join(terms8dot6)
                finalString += ";" + selectionText8dot6 + ";"


    with st.expander("Instruction/Training:", expanded = False):
        terms9 = st.multiselect("Choose all that apply:", ["General Instruction", "Physical Training", "Band Training/Center", "Military Training"])
        selectionText9 = ";".join(terms9)
        finalString += selectionText9

        if "General Instruction" in terms9:
            with st.expander("General Instruction", expanded = True):
                terms9dot1 = st.multiselect("Choose all that apply:", ["General Purpose Instruction", "Classroom", "Lecture Hall", "Training Facility", "Training Classroom", "Training Simulator"])
                selectionText9dot1 = ";".join(terms9dot1)
                finalString += ";" + selectionText9dot1 + ";"

        if "Physical Training" in terms9:
            with st.expander("Physical Training", expanded = True):
                terms9dot2 = st.multiselect("Choose all that apply:", ["Physical Education", "Natatorium"])
                selectionText9dot2 = ";".join(terms9dot2)
                finalString += ";" + selectionText9dot2 + ";"

        if "Military Training" in terms9:
            with st.expander("Military Training", expanded = True):
                terms9dot3 = st.multiselect("Choose all that apply:", ["Range", "Navigation Training", "Observation Bunker", "Maneuver Area", "Training Land", "Training Area", "Impact Area", "Parade Field", "Drill Field", "Obstacle Course", "Battle Course", "Assault Course", "Infiltration Course", "Gunnery Complex", "Traning Mock-ups", "Warfare Area"])
                selectionText9dot3 = ";".join(terms9dot3)
                finalString += ";" + selectionText9dot3 + ";"


    with st.expander("Maintenance:", expanded = False):
        terms10 = st.multiselect("Choose all that apply:", ["Maintenance Facility", "Corrosion Control Hangar", "Engine Test/Storage Facility", "Missile Maintenance Facility", "Watercraft Maintenance Facility", "Crane", "Wash Facility", "Inspection Shop"])
        selectionText10 = ";".join(terms10)
        finalString += selectionText10

        if "Maintenance Facility" in terms10:
            with st.expander("Maintenance Facility", expanded = True):
                terms10dot1 = st.multiselect("Choose all that apply:", ["Maintenance Hangar", "Maintenance Shop", "Maintenance Depot", "Maintenance Shed"])
                selectionText10dot1 = ";".join(terms10dot1)
                finalString += ";" + selectionText10dot1 + ";"

        if "Missile Maintenance Facility" in terms10:
            with st.expander("Missile Maintenance Facility", expanded = True):
                terms10dot2 = st.multiselect("Choose all that apply:", ["Missile Assembly Building", "Missile Maintenance Support Facility", "Launcher Maintenance Support Facility", "Missile Test Tower"])
                selectionText10dot2 = ";".join(terms10dot2)
                finalString += ";" + selectionText10dot2 + ";"

        if "Watercraft Maintenance Facility" in terms10:
            with st.expander("Watercraft Maintenance Facility", expanded = True):
                terms10dot3 = st.multiselect("Choose all that apply:", ["Dry-dock", "Maintenance Dock", "Marine Maintenance Shop", "Ship Maintenance Shop", "Marine Maintenance Support Facility"])
                selectionText10dot3 = ";".join(terms10dot3)
                finalString += ";" + selectionText10dot3 + ";"

        if "Crane" in terms10:
            with st.expander("Crane", expanded = True):
                terms10dot4 = st.multiselect("Choose all that apply:", ["Gantry Crane", "Bridge Crane"])
                selectionText10dot4 = ";".join(terms10dot4)
                finalString += ";" + selectionText10dot4 + ";"


    with st.expander("Marina/Harbor:", expanded = False):
        terms11 = st.multiselect("Choose all that apply:", ["Berthing Facility", "Boat Storage", "Water Launch Ramp", "Waterfront Improvements"])
        selectionText11 = ";".join(terms11)
        finalString += selectionText11

        if "Berthing Facility" in terms11:
            with st.expander("Berthing Facility", expanded = True):
                terms11dot1 = st.multiselect("Choose all that apply:", ["Pier", "Wharf", "Berthing", "Mooring"])
                selectionText11dot1 = ";".join(terms11dot1)
                finalString += ";" + selectionText11dot1 + ";"

        if "Boat Storage" in terms11:
            with st.expander("Boat Storage", expanded = True):
                terms11dot2 = st.multiselect("Choose:", ["Small Craft Building"])
                selectionText11dot2 = ";".join(terms11dot2)
                finalString += ";" + selectionText11dot2 + ";"


    with st.expander("Medical:", expanded = False):
        terms12 = st.multiselect("Choose all that apply:", ["Hospital", "Medical Laboratory", "Morgue/Mortuary", "Veterinary", "Clinic", "Pharmacy"])
        selectionText12 = ";".join(terms12)
        finalString += selectionText12

        if "Hospital" in terms12:
            with st.expander("Hospital", expanded = True):
                terms12dot1 = st.multiselect("Choose all that apply:", ["Infirmary", "Surgical Service"])
                selectionText12dot1 = ";".join(terms12dot1)
                finalString += ";" + selectionText12dot1 + ";"

        if "Medical Laboratory" in terms12:
            with st.expander("Medical Laboratory", expanded = True):
                terms12dot2 = st.multiselect("Choose all that apply:", ["Blood Processing Laboratory", "Drug Abuse Detection Laboratory", "Clinical Laboratory", "Dental Laboratory", "Medical Buliding", "Medical Warehouse"])
                selectionText12dot2 = ";".join(terms12dot2)
                finalString += ";" + selectionText12dot2 + ";"

        if "Veterinary" in terms12:
            with st.expander("Veterinary", expanded = True):
                terms12dot3 = st.multiselect("Choose all that apply:", ["Veterinary Clinic", "Animal Facility", "Animal Building"])
                selectionText12dot3 = ";".join(terms12dot3)
                finalString += ";" + selectionText12dot3 + ";"

        if "Clinic" in terms12:
            with st.expander("Clinic", expanded = True):
                terms12dot4 = st.multiselect("Choose all that apply:", ["Dental Clinic", "Abulatory Care Clinic", "Veterinary Clinic"])
                selectionText12dot4 = ";".join(terms12dot4)
                finalString += ";" + selectionText12dot4 + ";"

        if "Pharmacy" in terms12:
            with st.expander("Pharmacy", expanded = True):
                terms12dot5 = st.multiselect("Choose:", ["Dispensary"])
                selectionText12dot5 = ";".join(terms12dot5)
                finalString += ";" + selectionText12dot5 + ";"


    with st.expander("Military Defense:", expanded = False):
        terms13 = st.multiselect("Choose all that apply:", ["Operations Facility", "Fire Observation Tower", "Air Defense Facility", "Air Control Tower", "Security Guard Facility", "Terminal", "Aircarft Shelter"])
        selectionText13 = ";".join(terms13)
        finalString += selectionText13

        if "Operations Facility" in terms13:
            with st.expander("Operations Facility", expanded = True):
                terms13dot1 = st.multiselect("Choose all that apply:", ["Air Defense Operations Building", "Missile Operations Building", "Emergency Operations Center", "Base Operations", "Command Post", "Ship Operations Building", "Operations Support Building", "Security Force Building"])
                selectionText13dot1 = ";".join(terms13dot1)
                finalString += ";" + selectionText13dot1 + ";"

        if "Air Defense Facility" in terms13:
            with st.expander("Air Defense Facility", expanded = True):
                terms13dot2 = st.multiselect("Choose all that apply:", ["Strategic Missile Launch Facility", "Missile Guidance/Defense/Control Facility", "Missile Access Shaft/Tunnel", "Aircraft Arresting System", "Weapons Support Facility", "Explosive Ordnance Disposal", "Radar Tower", "Bunker"])
                selectionText13dot2 = ";".join(terms13dot2)
                finalString += ";" + selectionText13dot2 + ";"


    with st.expander("Production Plants:", expanded = False):
        terms14 = st.multiselect("Choose all that apply:", ["Production Plant", "Demineralization Plant"])
        selectionText14 = ";".join(terms14)
        finalString += selectionText14

        if "Production Plant" in terms14:
            with st.expander("Production Plant", expanded = True):
                terms14dot1 = st.multiselect("Choose all that apply:", ["Production Structure", "Asphalt Plant", "Concrete Plant", "Rock Crusher Plant"])
                selectionText14dot1 = ";".join(terms14dot1)
                finalString += ";" + selectionText14dot1 + ";"


    with st.expander("Research, Development, Testing and Evaluation:", expanded = False):
        terms15 = st.multiselect("Choose all that apply:", ["RDT&E Facility", "Wind Tunnel", "Engine Test Cell", "Observation Building", "Research Engineering Facility", "Test Facility", "Missile Instrumentation Facility"])
        selectionText15 = ";".join(terms15)
        finalString += selectionText15

        if "RDT&E Facility" in terms15:
            with st.expander("RDT&E Facility", expanded = True):
                terms15dot1 = st.multiselect("Choose all that apply:", ["RDT&E Laboratory", "RDT&E Building", "RDT&E Complex", "RDT&E Area", "RDT&E Range Building", "RDT&E Range Facility", "RDT&E Range Complex", "RDT&E Range Area", "RDT&E Technical Service Facility"])
                selectionText15dot1 = ";".join(terms15dot1)
                finalString += ";" + selectionText15dot1 + ";"

        if "Research Engineering Facility" in terms15:
            with st.expander("Medical Laboratory", expanded = True):
                terms15dot2 = st.multiselect("Choose:", ["Research Engineering Building"])
                selectionText15dot2 = ";".join(terms15dot2)
                finalString += ";" + selectionText15dot2 + ";"

        if "Test Facility" in terms15:
            with st.expander("Test Facility", expanded = True):
                terms15dot3 = st.multiselect("Choose all that apply:", ["Test Track", "Test Structure", "Test Stand", "Test Range Complex"])
                selectionText15dot3 = ";".join(terms15dot3)
                finalString += ";" + selectionText15dot3 + ";"

        if "Missile Instrumentation Facility" in terms15:
            with st.expander("Missile Instrumentation Facility", expanded = True):
                terms15dot4 = st.multiselect("Choose all that apply:", ["Missile Radar Station", "Missile Theodolite Station", "Missile Communications Station"])
                selectionText15dot4 = ";".join(terms15dot4)
                finalString += ";" + selectionText15dot4 + ";"


    with st.expander("Storm Water and Boundary Infrastructure:", expanded = False):
        terms16 = st.multiselect("Choose all that apply:", ["Storm Management Facilities", "Navigation Revetment", "Fish Facility", "Monitoring Well", "Fences/Barriers"])
        selectionText16 = ";".join(terms16)
        finalString += selectionText16

        if "Storm Management Facilities" in terms16:
            with st.expander("Storm Management Facilities", expanded = True):
                terms16dot1 = st.multiselect("Choose all that apply:", ["Storm Drainage", "Retaining Wall/Structure", "Swale", "Drainage Ditch", "Dam", "Lock", "Levee", "Dike", "Floodwall", "Storm Water Pond", "Storm Water Filtration", "Storm Water Treatment Structure", "Flood Control Structure", "Permeable Surface"])
                selectionText16dot1 = ";".join(terms16dot1)
                finalString += ";" + selectionText16dot1 + ";"

        if "Fences/Barriers" in terms16:
            with st.expander("Medical Laboratory", expanded = True):
                terms16dot2 = st.multiselect("Choose all that apply:", ["Boundary Fence", "Perimeter", "Security Fence", "Vehicle Barrier"])
                selectionText16dot2 = ";".join(terms16dot2)
                finalString += ";" + selectionText16dot2 + ";"


    with st.expander("Transportation Infrastructure:", expanded = False):
        terms17 = st.multiselect("Choose all that apply:", ["Vehicular Facilities", "Pedestrian", "Railroad Facilities"])
        selectionText17 = ";".join(terms17)
        finalString += selectionText17

        if "Vehicular Facilities" in terms17:
            with st.expander("Vehicular Facilities", expanded = True):
                terms17dot1 = st.multiselect("Choose all that apply:", ["Road", "Vehicular Bridge", "Tunnel", "Curbs and Gutters", "Driveway", "Parking Lot", "Parking Garage", "Garage Structure", "Parking Compound", "Staging Area", "Traffic Control Signals", "Traffic Lights", "Paved Area", "Laydown Area"])
                selectionText17dot1 = ";".join(terms17dot1)
                finalString += ";" + selectionText17dot1 + ";"

        if "Pedestrian" in terms17:
            with st.expander("Pedestrian", expanded = True):
                terms17dot2 = st.multiselect("Choose all that apply:", ["Sidewalk", "Walkway", "Pedestrian Bridge"])
                selectionText17dot2 = ";".join(terms17dot2)
                finalString += ";" + selectionText17dot2 + ";"

        if "Railroad Facilities" in terms17:
            with st.expander("Test Facility", expanded = True):
                terms17dot3 = st.multiselect("Choose all that apply:", ["Railroad Track", "Railroad Bridge", "Railroad Facility", "Railroad Spur"])
                selectionText17dot3 = ";".join(terms17dot3)
                finalString += ";" + selectionText17dot3 + ";"


    with st.expander("Utilities Infrastructure:", expanded = False):
        terms18 = st.multiselect("Choose all that apply:", ["Electrical/Power Facilities", "Gas Facilities", "Water Facilities", "Sewer/Water Treatment Facilities", "Telecommunication Facilities", "Industrial Waste Treatment", "Solid Waste Facilities"])
        selectionText18 = ";".join(terms18)
        finalString += selectionText18

        if "Electrical/Power Facilities" in terms18:
            with st.expander("Electrical/Power Facilities", expanded = True):
                terms18dot1 = st.multiselect("Choose all that apply:", ["Power Source/Substations/Switching Station", "Power Distribution/Overhead/Aerial/Buried Lines", "Wind Turbine", "Solar Collection System", "Transformer Station"])
                selectionText18dot1 = ";".join(terms18dot1)
                finalString += ";" + selectionText18dot1 + ";"

        if "Gas Facilities" in terms18:
            with st.expander("Gas Facilities", expanded = True):
                terms18dot2 = st.multiselect("Choose all that apply:", ["Gas Lines", "Gas Storage", "Gas Mains"])
                selectionText18dot2 = ";".join(terms18dot2)
                finalString += ";" + selectionText18dot2 + ";"

        if "Water Facilities" in terms18:
            with st.expander("Water Facilities", expanded = True):
                terms18dot3 = st.multiselect("Choose all that apply:", ["Potable Water Lines", "Non-potable Water Lines", "Cisterns", "Well", "Water Tanks", "Water Treatment", "Water Storage", "Water Distribution System", "Water Pump", "Water Impoundment", "Water Tanks", "Desalinization Plant", "Fountain", "Pond", "Reservoir"])
                selectionText18dot3 = ";".join(terms18dot3)
                finalString += ";" + selectionText18dot3 + ";"

        if "Sewer/Water Treatment Facilities" in terms18:
            with st.expander("Sewer/Water Treatment Facilities", expanded = True):
                terms18dot4 = st.multiselect("Choose all that apply:", ["Sewer Treatment Plant", "Sewer Treatment Lines", "Sewer Treatment Lift Station", "Septic Tank", "Drain Field", "Lagoon", "Settlement Pond"])
                selectionText18dot4 = ";".join(terms18dot4)
                finalString += ";" + selectionText18dot4 + ";"

        if "Telecommunication Facilities" in terms18:
            with st.expander("Telecommunication Facilities", expanded = True):
                terms18dot5 = st.multiselect("Choose all that apply:", ["Telecomm Lines", "Antenna", "Tower"])
                selectionText18dot5 = ";".join(terms18dot5)
                finalString += ";" + selectionText18dot5 + ";"

        if "Solid Waste Facilities" in terms18:
            with st.expander("Solid Waste Facilities", expanded = True):
                terms18dot6 = st.multiselect("Choose all that apply:", ["Refuse Collection", "Recycling Facility", "Structure", "Incinerator", "Landfill"])
                selectionText18dot6 = ";".join(terms18dot6)
                finalString += ";" + selectionText18dot6 + ";"

stringCleaned = re.sub(r';+', ';', finalString)
st.text_area (
    label = "Selected Facility Terms",
    value = stringCleaned.rstrip(";"),
    height = 300
)

copy_button (
    stringCleaned.rstrip(";"),
    tooltip = "Copy to Clipboard",
    copied_label = "Copied!",
    icon = "st"
)


st.subheader("Construction Material")
with st.expander("Construction Material", expanded = False):
    with st.expander("Construction Material:", expanded = False):
        terms19 = st.multiselect("Choose all that apply:", ["Concrete", "Cement", "Masonry", "Metal", "Mortar", "Plaster", "Wood"])
        selectionText19 = ";".join(terms19)
        finalMatsString += selectionText19

        if "Masonry" in terms19:
            with st.expander("Masonry", expanded = True):
                terms19dot1 = st.multiselect("Choose all that apply:", ["Brick", "Clay Tile", "Granite", "Limestone", "Sandstone"])
                selectionText19dot1 = ";".join(terms19dot1)
                finalMatsString += ";" + selectionText19dot1 + ";"

matsStringCleaned = re.sub(r';+', ';', finalMatsString)
st.text_area (
    label = "Selected Materials Terms",
    value = matsStringCleaned.rstrip(";"),
    height = 150
)

copy_button (
    matsStringCleaned.rstrip(";"),
    tooltip = "Copy to Clipboard",
    copied_label = "Copied!",
    icon = "st"
)


st.subheader("Time Periods")
with st.expander("Time Periods", expanded = False):
    with st.expander("Time Periods:", expanded = False):
        terms20 = st.multiselect("Choose all that apply:", ["Pre-Civil War", "Civil War", "World War I", "Interwar", "World War II", "Cold War", "Korean War", "Vietnam War", "18th Century", "19th Century", "20th Century", "21st Century"])
        selectionText20 = ";".join(terms20)
        finalTimeString += selectionText20

        if "Pre-Civil War" in terms20:
            with st.expander("Pre-Civil War", expanded = True):
                terms20dot1 = st.multiselect("Choose all that apply:", ["American Indian War", "Mexican-American War", "British Colonial", "Colonial Period", "Spanish Period", "Second Spanish Period", "Spanish Exploration", "Spanish Colonization", "Spanish Colonies", "Spanish Exploration and Colonization", "Pioneer Period", "Homestead Period", "Westward Expansion", "Santa Fe Trail", "Oregon Trail"])
                selectionText20dot1 = ";".join(terms20dot1)
                finalTimeString += ";" + selectionText20dot1 + ";"

        if "Civil War" in terms20:
            with st.expander("Civil War", expanded = True):
                terms20dot2 = st.multiselect("Choose all that apply:", ["Civil War Era", "American Indian War"])
                selectionText20dot2 = ";".join(terms20dot2)
                finalTimeString += ";" + selectionText20dot2 + ";"

        if "World War I" in terms20:
            with st.expander("World War I", expanded = True):
                terms20dot3 = st.multiselect("Choose:", ["WWI"])
                selectionText20dot3 = ";".join(terms20dot3)
                finalTimeString += ";" + selectionText20dot3 + ";"

        if "Interwar" in terms20:
            with st.expander("Interwar", expanded = True):
                terms20dot4 = st.multiselect("Choose all that apply:", ["Great Depression", "Pre-World War II"])
                selectionText20dot4 = ";".join(terms20dot4)
                finalTimeString += ";" + selectionText20dot4 + ";"

        if "World War II" in terms20:
            with st.expander("World War II", expanded = True):
                terms20dot5 = st.multiselect("Choose all that apply:", ["WWII", "WWII Era"])
                selectionText20dot5 = ";".join(terms20dot5)
                finalTimeString += ";" + selectionText20dot5 + ";"

        if "Cold War" in terms20:
            with st.expander("Cold War", expanded = True):
                terms20dot6 = st.multiselect("Choose all that apply:", ["Cold War Era", "Post World War II", "Korean War", "Vietnam War"])
                selectionText20dot6 = ";".join(terms20dot6)
                finalTimeString += ";" + selectionText20dot6 + ";"

        if "18th Century" in terms20:
            with st.expander("18th Century", expanded = True):
                terms20dot7 = st.multiselect("Choose all that apply:", ["1800s", "18th-19th Century", "18th-20th Centuries"])
                selectionText20dot7 = ";".join(terms20dot7)
                finalTimeString += ";" + selectionText20dot7 + ";"

        if "19th Century" in terms20:
            with st.expander("19th Century", expanded = True):
                terms20dot8 = st.multiselect("Choose all that apply:", ["1900s", "18th-19th Century", "18th-20th Centuries", "19th-20th Century", "Late 19th-20th Century"])
                selectionText20dot8 = ";".join(terms20dot8)
                finalTimeString += ";" + selectionText20dot8 + ";"

        if "20th Century" in terms20:
            with st.expander("20th Century", expanded = True):
                terms20dot9 = st.multiselect("Choose all that apply:", ["18th-20th Centuries", "19th-20th Century", "Late 19th-20th Century", "20th Century Military", "1920s", "1930s", "1940s", "1950s", "1960s"])
                selectionText20dot9 = ";".join(terms20dot9)
                finalTimeString += ";" + selectionText20dot9 + ";"

        if "21st Century" in terms20:
            with st.expander("21st Century", expanded = True):
                terms20dot10 = st.multiselect("Choose all that apply:", ["Homestead Era", "Territorial Period", "Westward Expansion", "Indian Wars", "Santa Fe Trail", "Oregon Trail"])
                selectionText20dot10 = ";".join(terms20dot10)
                finalTimeString += ";" + selectionText20dot10 + ";"

timeStringCleaned = re.sub(r';+', ';', finalTimeString)
st.text_area (
    label = "Selected Time Period Terms",
    value = timeStringCleaned.rstrip(";"),
    height = 150
)

copy_button (
    timeStringCleaned.rstrip(";"),
    tooltip = "Copy to Clipboard",
    copied_label = "Copied!",
    icon = "st"
)
