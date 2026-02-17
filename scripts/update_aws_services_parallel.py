#!/usr/bin/env python3
"""
Parallel AWS Service Documentation Updater

This script processes multiple AWS service documentation files in parallel
using multiprocessing to speed up the update process.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List, Tuple

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def get_services_needing_update() -> List[Tuple[str, str]]:
    """Get list of services that need updating (have minimal content)."""
    services = []
    aws_dir = project_root / "docs" / "aws"
    
    # List of services that still need updating
    # This can be populated from your analysis
    minimal_services = [
        # Compute
        ("compute/outposts", "Outposts"),
        ("compute/wavelength", "Wavelength"),
        ("compute/local_zones", "Local Zones"),
        ("compute/ec2_image_builder", "EC2 Image Builder"),
        ("compute/ec2_global_view", "EC2 Global View"),
        ("compute/amazon_linux", "Amazon Linux"),
        ("compute/parallel_computing", "Parallel Computing"),
        ("compute/parallel_cluster", "Parallel Cluster"),
        ("compute/simspace_weaver", "SimSpace Weaver"),
        ("compute/serverless_application_repository", "Serverless Application Repository"),
        
        # Networking
        ("networking_and_content_delivery/privatelink", "PrivateLink"),
        ("networking_and_content_delivery/global_accelerator", "Global Accelerator"),
        ("networking_and_content_delivery/cloud_map", "Cloud Map"),
        ("networking_and_content_delivery/app_mesh", "App Mesh"),
        ("networking_and_content_delivery/application_recovery_controller_arc", "Application Recovery Controller"),
        ("networking_and_content_delivery/verified_access", "Verified Access"),
        ("networking_and_content_delivery/site_to_site_vpn", "Site-to-Site VPN"),
        ("networking_and_content_delivery/client_vpn", "Client VPN"),
        ("networking_and_content_delivery/gateway_load_balancer", "Gateway Load Balancer"),
        ("networking_and_content_delivery/network_load_balancer", "Network Load Balancer"),
        ("networking_and_content_delivery/application_load_balancer", "Application Load Balancer"),
        
        # Security
        ("security/directory_service", "Directory Service"),
        ("security/identity_center", "Identity Center"),
        ("security/detective", "Detective"),
        ("security/firewall_manager", "Firewall Manager"),
        ("security/cloud_directory", "Cloud Directory"),
        
        # Machine Learning
        ("machine_learning/codeguru", "CodeGuru"),
        ("machine_learning/forecast", "Forecast"),
        ("machine_learning/healthlake", "HealthLake"),
        ("machine_learning/lookout", "Lookout"),
        ("machine_learning/monitron", "Monitron"),
        ("machine_learning/panorama", "Panorama"),
        ("machine_learning/deepracer", "DeepRacer"),
        ("machine_learning/deepcomposer", "DeepComposer"),
        
        # Management & Governance
        ("management_and_governance/compute_optimizer", "Compute Optimizer"),
        ("management_and_governance/resilience_hub", "Resilience Hub"),
        ("management_and_governance/proton", "Proton"),
        ("management_and_governance/appconfig", "AppConfig"),
        ("management_and_governance/q_developer", "Q Developer"),
        
        # Developer Tools
        ("developer_tools/codecatalyst", "CodeCatalyst"),
        ("developer_tools/command_line", "Command Line"),
        ("developer_tools/corretto", "Corretto"),
        ("developer_tools/fault_injection_service", "Fault Injection Service"),
        ("developer_tools/infrastructure_composer", "Infrastructure Composer"),
        ("developer_tools/microservice_extractor", "Microservice Extractor"),
        ("developer_tools/porting_assistant", "Porting Assistant"),
        ("developer_tools/q_developer", "Q Developer"),
        ("developer_tools/app_studio", "App Studio"),
        
        # General Reference
        ("general_reference/diagnostic_tools", "Diagnostic Tools"),
        ("general_reference/service_endpoints", "Service Endpoints"),
        ("general_reference/service_quotas_reference", "Service Quotas Reference"),
        ("general_reference/security_credentials", "Security Credentials"),
        ("general_reference/tagging_aws_resources", "Tagging AWS Resources"),
        
        # Other
        ("game_development/gamelift", "GameLift"),
        ("quantum_computing/braket", "Braket"),
        ("satellite/ground_station", "Ground Station"),
    ]
    
    for rel_path, service_name in minimal_services:
        full_path = aws_dir / rel_path / "index.md"
        if full_path.exists():
            services.append((str(full_path), service_name))
    
    return services

def update_service_documentation(service_path: str, service_name: str) -> Tuple[str, bool, str]:
    """
    Update a single service documentation file.
    Returns: (service_name, success, message)
    """
    try:
        # This would call your documentation generation logic
        # For now, this is a placeholder that shows the structure
        
        # In a real implementation, you would:
        # 1. Search for service information
        # 2. Generate comprehensive documentation
        # 3. Write to file
        
        print(f"Processing {service_name}...")
        
        # Placeholder - replace with actual update logic
        # You could call a function that uses web_search and write operations
        
        return (service_name, True, f"Updated {service_name}")
    except Exception as e:
        return (service_name, False, str(e))

def main():
    """Main function to process services in parallel."""
    services = get_services_needing_update()
    
    if not services:
        print("No services found that need updating.")
        return
    
    print(f"Found {len(services)} services to update.")
    print(f"Processing with {os.cpu_count()} parallel workers...")
    
    # Process services in parallel
    results = []
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        # Submit all tasks
        future_to_service = {
            executor.submit(update_service_documentation, path, name): (path, name)
            for path, name in services
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_service):
            path, name = future_to_service[future]
            try:
                result = future.result()
                results.append(result)
                service_name, success, message = result
                status = "✓" if success else "✗"
                print(f"{status} {service_name}: {message}")
            except Exception as e:
                print(f"✗ Error processing {name}: {e}")
                results.append((name, False, str(e)))
    
    # Summary
    successful = sum(1 for _, success, _ in results if success)
    failed = len(results) - successful
    
    print(f"\n{'='*60}")
    print(f"Summary: {successful} successful, {failed} failed")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
