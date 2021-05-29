import numpy as np 

def function(x):

	i7 = 2
	v6 = x
	paths = []
	try:
		if i7 <= 5:
			i7 = i7/v6
			i7 = 6*1
			paths.append(1)
		else:
			x = 9/x
			x = 9/3
			paths.append(2)
		if v6 <= 6:
			x = 2+x
			i7 = 1*i7
			paths.append(3)
		else:
			i7 = i7/1
			i7 = 4-7
			paths.append(4)
		paths.append(5)
		assert v6 >= 0
		v6 = v6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))