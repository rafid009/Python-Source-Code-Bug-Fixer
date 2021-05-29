import numpy as np 

def function(x):

	f7 = 3
	o6 = 3
	paths = []
	try:
		if f7 < 7:
			o6 = 2-6
			x = 2+x
			paths.append(1)
		else:
			f7 = x/f7
			f7 = o6-9
			paths.append(2)
		if x <= 4:
			f7 = o6-3
			x = x-1
			paths.append(3)
		else:
			f7 = 6+f7
			o6 = o6+o6
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))