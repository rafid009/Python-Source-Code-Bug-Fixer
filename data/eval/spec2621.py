import numpy as np 

def function(x):

	i7 = 3
	f3 = x
	paths = []
	try:
		if i7 <= 9:
			x = x/x
			paths.append(1)
		else:
			f3 = x+x
			i7 = x-i7
			f3 = 9-9
			paths.append(2)
		if x > 2:
			f3 = f3-4
			x = 1/6
			paths.append(3)
		else:
			x = x*0
			i7 = i7/i7
			i7 = i7+7
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		i7 = f3**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))