import numpy as np 

def function(x):

	x6 = 7
	v9 = x
	paths = []
	try:
		if x < 7:
			x = x+x6
			v9 = x6-x
			v9 = x*x6
			paths.append(1)
		else:
			v9 = 2*0
			x6 = x6*4
			paths.append(2)
		if v9 < 4:
			v9 = 8-v9
			x6 = 6+x6
			v9 = 8-x
			paths.append(3)
		else:
			x = v9+x
			x = 2*0
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		x = v9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))