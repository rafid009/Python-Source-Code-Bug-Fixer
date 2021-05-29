import numpy as np 

def function(x):

	t9 = x
	f7 = 1
	paths = []
	try:
		if x >= 4:
			f7 = f7-0
			paths.append(1)
		else:
			x = 9/1
			x = x*0
			paths.append(2)
		if t9 <= 1:
			f7 = f7+f7
			x = 2+f7
			paths.append(3)
		else:
			f7 = f7-f7
			x = x-0
			t9 = 3+9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		f7 = t9**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))