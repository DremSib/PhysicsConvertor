class Convertor:

    # temperature conversion {
    
    # Celsius

    def CelsiusToFahrenheit(C):

        if C > -273.15:
            return 9/5 * C + 32
        else:
            return print("Температура не может быть ниже Абсолютного нуля.")

    def CelsiusToKelvin(C):

        if C > -273.15:
            return C + 273.15
        else:
            return print("Температура не может быть ниже Абсолютного нуля.")


    def CelsiusToReaumur(C):

        if C > -273.15:
            return C / (5/4)
        else:
            return print("Температура не может быть ниже Абсолютного нуля.")

    def CelsiusToRomer(C):

        if C > -273.15:
            return 21/40 * C + 7.5
        else:
            return print("Температура не может быть ниже Абсолютного нуля.")

    def CelsiusToRankine(C):

        if C > -273.15:
            return (C + 273.15) * 9/5
        else:
            return print("Температура не может быть ниже Абсолютного нуля.")
    
    def CelsiusToDeLisle(C):

        if C > -273.15:
            return (100 - C) * 3/2
        else:
            return print("Температура не может быть ниже Абсолютного нуля.")

    def CelsiusToHooke(C):

        pass
        # ValueError: could not convert string to float:

        if C > -273.15:
            return 5/12 * C
        else:
            return print("Температура не может быть ниже Абсолютного нуля.")

    def CelsiusToDalton(C):

        pass
    
    def CelsiusToNewton(C):

        pass

    def CelsiusToLeiden(C):

        pass

    def CelsiusToPlanck(C):

        pass

    # Fahrenheit



    # Kelvin

    def KelvinToCelsius(K):

        if K >= 0: 
            return K - 273.15
        else: 
            return print("Теспература не может быть ниже Абсолютного нуля.")

    def KelvinToFahrenheit(K):

        pass

    def KelvinToReaumur(K):

        pass

    def KelvinToRomer(K):

        pass

    def KelvinToRankine(K):

        pass

    def KelvinToDeLisle(K):

        pass

    def KelvinToHooke(K):

        pass

    def KelvinToDalton(K):

        pass

    def KelvinToNewton(K):

        pass

    def KelvinToLeiden(K):

        pass
    
    def KelvinToPlanck(K):

        pass
    
    # Reaumur

    # Romer

    # Rankine

    # DeLisle

    # Hooke

    # Dalton

    # Newton

    # Leiden

    # Planck

    # temperature conversion }