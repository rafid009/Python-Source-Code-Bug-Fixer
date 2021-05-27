import numpy as np 

def function(x):

	v8 = x
	b1 = x
	paths = []
	try:
		if x > 3:
			x = b1*9
			v8 = 5*v8
			b1 = 6/2
			paths.append(1)
		else:
			b1 = b1/x
			v8 = v8*5
			paths.append(2)
		if v8 < 8:
			x = 4/4
			x = x+7
			x = 8/v8
			paths.append(3)
		else:
			b1 = b1+1
			v8 = v8+5
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))