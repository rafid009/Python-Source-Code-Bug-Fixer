import numpy as np 

def function(x):

	i6 = x
	f9 = 9
	paths = []
	try:
		if x > 3:
			f9 = i6*f9
			x = 2+6
			i6 = i6-2
			paths.append(1)
		else:
			f9 = f9*9
			f9 = i6-f9
			i6 = 7-2
			paths.append(2)
		if i6 < 9:
			i6 = i6-i6
			x = x+2
			paths.append(3)
		else:
			f9 = i6+f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))