import numpy as np 

def function(x):

	b9 = x
	v3 = 6
	paths = []
	try:
		if b9 < 7:
			b9 = b9+1
			b9 = b9*5
			paths.append(1)
		else:
			v3 = 8+7
			paths.append(2)
		if v3 > 1:
			x = x*x
			v3 = 8+0
			v3 = v3*b9
			paths.append(3)
		else:
			b9 = b9*x
			v3 = 2+v3
			v3 = 5/2
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))