import streamlit as st

def convert_length(value, from_unit, to_unit):
    # Base unit is meters
    to_meters = {
        "Meters": 1,
        "Kilometers": 1000,
        "Miles": 1609.34,
        "Feet": 0.3048,
        "Inches": 0.0254,
        "Centimeters": 0.01,
        "Yards": 0.9144
    }
    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    return result

def convert_weight(value, from_unit, to_unit):
    # Base unit is grams
    to_grams = {
        "Grams": 1,
        "Kilograms": 1000,
        "Pounds": 453.592,
        "Ounces": 28.3495,
        "Milligrams": 0.001,
        "Metric Tons": 1000000
    }
    grams = value * to_grams[from_unit]
    result = grams / to_grams[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return ((value - 273.15) * 9/5) + 32
    return value

def convert_digital(value, from_unit, to_unit):
    # Base unit is bytes
    to_bytes = {
        "Bytes": 1,
        "Kilobytes": 1024,
        "Megabytes": 1024**2,
        "Gigabytes": 1024**3,
        "Terabytes": 1024**4,
        "Petabytes": 1024**5
    }
    bytes_val = value * to_bytes[from_unit]
    result = bytes_val / to_bytes[to_unit]
    return result

def convert_time(value, from_unit, to_unit):
    # Base unit is seconds
    to_seconds = {
        "Seconds": 1,
        "Minutes": 60,
        "Hours": 3600,
        "Days": 86400,
        "Weeks": 604800,
        "Months": 2592000,  # Approximate (30 days)
        "Years": 31536000   # Non-leap year
    }
    seconds = value * to_seconds[from_unit]
    result = seconds / to_seconds[to_unit]
    return result

def convert_speed(value, from_unit, to_unit):
    # Base unit is meters per second
    to_mps = {
        "Meters per second": 1,
        "Kilometers per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Knots": 0.514444,
        "Feet per second": 0.3048
    }
    mps = value * to_mps[from_unit]
    result = mps / to_mps[to_unit]
    return result

def main():
    st.title("Unit Converter")
    st.markdown("### Convert between multiple units")
    
    # Select conversion type
    conversion_type = st.selectbox(
        "Select what to convert",
        ["Length", "Weight", "Temperature", "Digital Storage", "Time", "Speed"]
    )
    
    # Dictionary of units for each conversion type
    units = {
        "Length": ["Meters", "Kilometers", "Miles", "Feet", "Inches", "Centimeters", "Yards"],
        "Weight": ["Grams", "Kilograms", "Pounds", "Ounces", "Milligrams", "Metric Tons"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Digital Storage": ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"],
        "Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"],
        "Speed": ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots", "Feet per second"]
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        from_unit = st.selectbox("From:", units[conversion_type])
        value = st.number_input("Enter value:", value=0.0)
        
    with col2:
        to_unit = st.selectbox("To:", units[conversion_type])
    
    if st.button("Convert"):
        try:
            if conversion_type == "Length":
                result = convert_length(value, from_unit, to_unit)
            elif conversion_type == "Weight":
                result = convert_weight(value, from_unit, to_unit)
            elif conversion_type == "Temperature":
                result = convert_temperature(value, from_unit, to_unit)
            elif conversion_type == "Digital Storage":
                result = convert_digital(value, from_unit, to_unit)
            elif conversion_type == "Time":
                result = convert_time(value, from_unit, to_unit)
            elif conversion_type == "Speed":
                result = convert_speed(value, from_unit, to_unit)
                
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
        except Exception as e:
            st.error("An error occurred during conversion. Please check your input.")

    # Add information section
    with st.expander("ℹ️ About"):
        st.markdown("""
        ### New Features Added:
        - Digital Storage conversions (Bytes to Petabytes)
        - Time conversions (Seconds to Years)
        - Speed conversions (various units)
        - More length and weight units
        - Improved precision in calculations
        
        ### How to use:
        1. Select the conversion type
        2. Choose your input and output units
        3. Enter the value
        4. Click Convert
        """)

if __name__ == "__main__":
    main()
 