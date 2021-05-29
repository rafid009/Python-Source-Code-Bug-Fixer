import numpy as np 

def function(x):

	i2 = x
	r5 = 6
	paths = []
	try:
		if r5 <= 1:
			i2 = x*0
			i2 = i2+6
			paths.append(1)
		else:
			x = x+7
			i2 = i2-2
			r5 = x*1
			paths.append(2)
		if r5 <= 2:
			i2 = i2*x
			r5 = r5*5
			x = 5-7
			paths.append(3)
		else:
			i2 = 1*7
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		r5 = i2**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))