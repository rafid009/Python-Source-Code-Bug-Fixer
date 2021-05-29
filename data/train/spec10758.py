import numpy as np 

def function(x):

	f2 = 3
	t4 = 4
	paths = []
	try:
		if t4 <= 0:
			f2 = f2+6
			paths.append(1)
		else:
			f2 = 7+f2
			x = x+9
			paths.append(2)
		if t4 < 4:
			x = 0*t4
			x = x+3
			t4 = 5/t4
			paths.append(3)
		else:
			f2 = f2*x
			t4 = t4+5
			t4 = 6-t4
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		f2 = f2**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))