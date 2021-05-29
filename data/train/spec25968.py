import numpy as np 

def function(x):

	k9 = 3
	v8 = 2
	paths = []
	try:
		if v8 < 9:
			x = x*2
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if v8 <= 8:
			v8 = v8*1
			v8 = 4*0
			paths.append(3)
		else:
			x = 7+x
			x = 8/k9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))