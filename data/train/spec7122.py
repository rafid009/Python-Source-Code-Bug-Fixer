import numpy as np 

def function(x):

	f6 = x
	t4 = 2
	paths = []
	try:
		if t4 >= 0:
			f6 = f6+t4
			f6 = x+t4
			t4 = 4+3
			paths.append(1)
		else:
			f6 = f6-f6
			x = f6+5
			f6 = 4/9
			paths.append(2)
		if f6 > 2:
			f6 = 0*7
			x = f6+f6
			f6 = f6+3
			paths.append(3)
		else:
			t4 = 9+6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		t4 = f6**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))