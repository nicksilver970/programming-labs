def heat_exchanger_step(t1_start, t1_end, t1_step, efficiency=0.55, threshold=60.0):
    """Рассчитывает температуру T2 от T1 в цикле for. При T2 > 60 °C моделирует включение доп. контура."""
    results = []
    n_steps = round((t1_end - t1_start) / t1_step) + 1

    for i in range(n_steps):
        t1 = t1_start + i * t1_step
        t2 = t1 * efficiency

        if t2 > threshold:
            t2 *= 0.85

        results.append((round(t1, 2), round(t2, 2)))

    return results


def main():
    """Точка входа в программу для вывода результатов расчета."""
    print("=== ТЕПЛООБМЕННИК: РАСЧЁТ ТЕМПЕРАТУРЫ T2 ===")
    pairs = heat_exchanger_step(t1_start=20.0, t1_end=140.0, t1_step=20.0)

    print("\nИтоговый список пар (T1, T2):")
    for t1, t2 in pairs:
        print(f"   T1 = {t1:>6.1f} °C    T2 = {t2:>6.2f} °C")


if __name__ == "__main__":
    main()
