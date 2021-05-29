import numpy as np 

def function(x):

	f1 = x
	i3 = x
	paths = []
	try:
		if f1 >= 0:
			i3 = i3/7
			paths.append(1)
		else:
			i3 = i3-8
			paths.append(2)
		if x >= 7:
			f1 = 7+f1
			i3 = i3*3
			f1 = 2-3
			paths.append(3)
		else:
			x = x/i3
			i3 = i3+5
			i3 = i3/4
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))