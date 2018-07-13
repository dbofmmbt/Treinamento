class Area
    def circulo(raio)
        return @raio * @raio * 3.14
    end

    def retangulo(base, altura)
        return @base*@altura
    end

    def quadrado(lado)
        return self.retangulo(lado, lado)
    end
    def trapezio(bmenor, bmaior, altura)
        return (@bmenor + @bmaior)/2 * @altura
    end

end

X = Area.new

puts X.circulo(5)
