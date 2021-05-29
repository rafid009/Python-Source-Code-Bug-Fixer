import numpy as np 

def function(x):

	v3 = x
	t4 = x
	paths = []
	try:
		if t4 <= 5:
			v3 = 2+9
			paths.append(1)
		else:
			v3 = 5+v3
			v3 = 0-x
			t4 = t4-4
			paths.append(2)
		if x >= 2:
			x = 8+x
			x = x+0
			paths.append(3)
		else:
			t4 = t4+2
			v3 = 5+x
			x = x+4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))