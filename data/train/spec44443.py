import numpy as np 

def function(x):

	i2 = x
	r2 = x
	paths = []
	try:
		if i2 < 2:
			x = x/6
			paths.append(1)
		else:
			i2 = x/i2
			i2 = 7-i2
			r2 = r2+1
			paths.append(2)
		if r2 > 0:
			i2 = 4+i2
			r2 = r2*2
			x = x/8
			paths.append(3)
		else:
			i2 = 6*0
			i2 = i2-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))