import numpy as np 

def function(x):

	a1 = x
	v8 = x
	paths = []
	try:
		if a1 > 7:
			v8 = x-4
			v8 = 1+7
			x = x+2
			paths.append(1)
		else:
			v8 = v8-1
			a1 = 6-a1
			paths.append(2)
		if a1 <= 0:
			v8 = v8*2
			v8 = 4-v8
			a1 = a1/4
			paths.append(3)
		else:
			v8 = 2*0
			v8 = 3-v8
			a1 = 8-a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))