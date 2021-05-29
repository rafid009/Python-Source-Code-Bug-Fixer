import numpy as np 

def function(x):

	t7 = 1
	m9 = x
	paths = []
	try:
		if t7 < 3:
			t7 = x+7
			paths.append(1)
		else:
			m9 = t7/m9
			m9 = t7+m9
			paths.append(2)
		if m9 < 4:
			m9 = 0/7
			x = m9*t7
			m9 = m9-9
			paths.append(3)
		else:
			t7 = 5-4
			x = x*0
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))