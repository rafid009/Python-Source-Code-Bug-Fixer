import numpy as np 

def function(x):

	e1 = x
	k7 = x
	x = 2
	paths = []
	try:
		if e1 >= 6:
			k7 = k7/e1
			k7 = 5/4
			paths.append(1)
		else:
			e1 = k7/e1
			e1 = 2+1
			paths.append(2)
		if e1 <= 4:
			k7 = k7-5
			e1 = e1+k7
			paths.append(3)
		else:
			e1 = e1+e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		k7 = e1**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))