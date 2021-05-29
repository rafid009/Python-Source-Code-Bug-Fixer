import numpy as np 

def function(x):

	i3 = x
	v8 = x
	paths = []
	try:
		if x > 9:
			v8 = v8-6
			i3 = 5-i3
			paths.append(1)
		else:
			x = x+5
			i3 = i3+7
			x = 6+x
			paths.append(2)
		if i3 > 9:
			v8 = i3/1
			x = v8/5
			paths.append(3)
		else:
			v8 = v8*5
			i3 = i3-6
			x = x*4
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x = i3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))