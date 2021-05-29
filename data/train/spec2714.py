import numpy as np 

def function(x):

	i3 = 9
	f9 = x
	paths = []
	try:
		if x < 3:
			i3 = i3*i3
			paths.append(1)
		else:
			f9 = 0-5
			i3 = i3-i3
			i3 = 6-f9
			paths.append(2)
		if f9 < 0:
			x = 0*x
			paths.append(3)
		else:
			x = 4*x
			i3 = f9+1
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