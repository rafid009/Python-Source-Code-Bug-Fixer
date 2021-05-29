import numpy as np 

def function(x):

	o8 = 5
	h1 = x
	paths = []
	try:
		if x > 7:
			h1 = h1*0
			o8 = 1-h1
			o8 = 6*o8
			paths.append(1)
		else:
			x = x*2
			o8 = o8*o8
			paths.append(2)
		if x < 8:
			o8 = o8-7
			x = 9+x
			paths.append(3)
		else:
			x = x/6
			o8 = 4/9
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		x = h1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))