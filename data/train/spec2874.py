import numpy as np 

def function(x):

	v7 = x
	f1 = x
	paths = []
	try:
		if f1 > 3:
			v7 = x*3
			paths.append(1)
		else:
			f1 = 9*0
			f1 = x+f1
			v7 = v7-3
			paths.append(2)
		if f1 > 9:
			x = x*v7
			x = v7+x
			paths.append(3)
		else:
			x = x-8
			f1 = 3+f1
			f1 = f1+1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		v7 = f1**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))