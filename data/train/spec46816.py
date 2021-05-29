import numpy as np 

def function(x):

	t0 = x
	i3 = 8
	paths = []
	try:
		if x <= 9:
			t0 = t0*6
			i3 = 1+i3
			x = 6+i3
			paths.append(1)
		else:
			i3 = x/6
			t0 = t0+5
			paths.append(2)
		if i3 <= 8:
			i3 = i3*4
			paths.append(3)
		else:
			t0 = t0/5
			t0 = t0-i3
			t0 = 3+t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		i3 = t0**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))