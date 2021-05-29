import numpy as np 

def function(x):

	f3 = x
	v6 = 8
	paths = []
	try:
		if x < 4:
			x = x+3
			v6 = v6-2
			f3 = f3/v6
			paths.append(1)
		else:
			v6 = v6/1
			v6 = v6+9
			paths.append(2)
		if x < 0:
			x = x*f3
			f3 = v6+f3
			paths.append(3)
		else:
			f3 = f3/1
			f3 = 5+7
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))