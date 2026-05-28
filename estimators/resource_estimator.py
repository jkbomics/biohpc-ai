def estimate_resources(config, total_data_size_gb):

    recommendations = config["recommendations"]

    base_ram = recommendations["base_ram_gb"]
    ram_factor = recommendations["ram_per_10gb_data"]

    ram = base_ram + (
        (total_data_size_gb / 10) * ram_factor
    )

    cpus = recommendations["recommended_threads"]

    runtime = (
        total_data_size_gb / 10
    ) * recommendations["runtime_per_10gb_hours"]

    return {
        "ram_gb": round(ram),
        "cpus": cpus,
        "runtime_hours": round(runtime, 2)
    }