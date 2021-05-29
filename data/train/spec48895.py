import numpy as np 

def function(x):

	i1 = x
	f1 = x
	paths = []
	try:
		if i1 <= 9:
			x = f1-3
			i1 = 1/i1
			f1 = f1+0
			paths.append(1)
		else:
			i1 = 6+i1
			paths.append(2)
		if f1 <= 9:
			i1 = i1*7
			x = 4/f1
			paths.append(3)
		else:
			i1 = 3*0
			i1 = f1/f1
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		i1 = i1**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))